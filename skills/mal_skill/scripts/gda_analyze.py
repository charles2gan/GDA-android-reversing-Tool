#!/usr/bin/env python3
"""
GDA.exe Socket-based Client for APK Analysis

GDA.exe runs as a server that accepts commands via socket connection.
This module provides functions to:
1. Start GDA server for an APK
2. Send commands and receive responses
3. Help AI perform analysis by running targeted commands

Usage:
    python gda_analyze.py <apk_file> [commands...]

Commands:
    binfo      - Base info
    pname      - Package name
    permission - Permissions
    axml       - AndroidManifest XML
    attsf      - Attack surface
    packer     - Packer info
    malscan    - Malware scan
    sensinf    - Sensitive info
    uri        - URI/paths
    appstr     - All strings
    api        - API methods
    native     - Native methods
    cert       - Certificate info
    interface  - Interface classes

Parametric commands (require arguments):
    header n           - DEX header (n=0,1,2...)
    listm cname        - List methods of class
    sclass cidx        - List subclasses
    pclass cidx        - List parent class
    dasm method@xxxxx   - Disassemble method
    dasm -n "signature" - Disassemble by signature
    dec -c classname   - Decompile class
    find -c/-m/-s name - Find objects
    xref -c/-m/-s name - Cross references

Examples:
    python gda_analyze.py sample.apk
    python gda_analyze.py sample.apk binfo permission axml
    python gda_analyze.py sample.apk --preset triage
    python gda_analyze.py sample.apk --preset malware
"""

import argparse
import locale
import os
import socket
import struct
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

# GDA.exe location
DEFAULT_GDA_EXE = Path(__file__).parent.parent / "bin" / "gda.exe"
DEFAULT_PORT_BASE = 10001
DEFAULT_PORT_MAX = 10999

# GDA server commands (no parameters needed)
GDA_COMMANDS = [
    "binfo",      # APK base info
    "pname",      # Package name
    "permission", # Permissions
    "axml",       # AndroidManifest.xml content
    "header",     # DEX header (requires n: header 0)
    "attsf",      # Attack surface
    "packer",     # Packer detection
    "cert",       # Certificate info
    "appstr",     # All strings
    "sensinf",    # Sensitive info
    "uri",        # URIs and paths
    "interface",  # Interface classes
    "native",     # Native methods
    "api",        # API methods
    "malscan",    # Malware scan
]

# Parametric GDA commands (require arguments)
GDA_PARAMETRIC_COMMANDS = [
    "listm",  # listm cname - List methods of class
    "sclass", # sclass cidx - List subclasses by class index
    "pclass", # pclass cidx - List parent class by class index
    "dasm",   # dasm method@xxxxx or dasm -n "signature"
    "dec",    # dec -c classname or dec method@xxxxx
    "find",   # find -c/-m/-s/-i/-a name
    "xref",   # xref -c/-m/-s/-f name or xref @type
]

# Analysis presets (only commands without parameters)
PRESETS = {
    "triage": ["binfo", "pname", "permission", "axml", "attsf"],
    "basic": ["binfo", "pname", "permission", "axml", "attsf", "cert"],
    "strings": ["appstr", "sensinf", "uri"],
    "malware": ["binfo", "pname", "permission", "axml", "attsf", "cert", "sensinf", "uri", "appstr", "api", "native"],
    "full": ["binfo", "pname", "permission", "axml", "header", "attsf", "packer", "cert", "appstr", "sensinf", "uri", "interface", "native", "api", "malscan"],
}


def decode_text_bytes(data: bytes) -> str:
    """Try to decode bytes to string using multiple encodings."""
    if not data:
        return ""
    candidates = ["utf-8", "utf-8-sig", "gb18030", locale.getpreferredencoding(False)]
    seen = set()
    for encoding in candidates:
        if not encoding or encoding.lower() in seen:
            continue
        seen.add(encoding.lower())
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    # Fallback: replace errors
    for encoding in candidates:
        if not encoding:
            continue
        try:
            return data.decode(encoding, errors="replace")
        except Exception:
            continue
    return data.decode("utf-8", errors="replace")


class GDASocketClient:
    """Client for communicating with GDA server via socket."""

    def __init__(self, host: str = "127.0.0.1", port: int = 8888, timeout: float = 60.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._sock: Optional[socket.socket] = None

    def connect(self) -> bool:
        """Connect to GDA server."""
        try:
            self._sock = socket.create_connection(
                (self.host, self.port),
                timeout=self.timeout
            )
            return True
        except OSError as e:
            print(f"[Error] Cannot connect to GDA server at {self.host}:{self.port}: {e}")
            return False

    def disconnect(self):
        """Disconnect from GDA server."""
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass
            self._sock = None

    def execute(self, cmd: str) -> str:
        """Execute a command and return the response."""
        # Auto-reconnect if not connected (GDA closes connection after each command)
        if not self._sock:
            if not self.connect():
                return "[Error] Cannot connect to GDA server"

        try:
            self._sock.sendall((cmd + "\n").encode("utf-8"))

            # Read response length (4-byte network order)
            length_data = self._recv_exact(self._sock, 4)
            if not length_data:
                return "[Error] No response length received"
            response_length = struct.unpack("!I", length_data)[0]

            # Read response payload
            payload = self._recv_exact(self._sock, response_length)

            # GDA closes connection after each command, so disconnect
            self.disconnect()

            return decode_text_bytes(payload)

        except Exception as e:
            self.disconnect()
            return f"[Error] Command '{cmd}' failed: {e}"

    @staticmethod
    def _recv_exact(sock: socket.socket, length: int) -> bytes:
        """Receive exact number of bytes."""
        chunks = []
        received = 0
        while received < length:
            chunk = sock.recv(length - received)
            if not chunk:
                raise RuntimeError("Connection closed while receiving data")
            chunks.append(chunk)
            received += len(chunk)
        return b"".join(chunks)


class GDAServerManager:
    """Manages GDA server process lifecycle."""

    def __init__(self, gda_exe_path: Path):
        self.gda_exe = gda_exe_path
        self.process: Optional[subprocess.Popen] = None
        self.port: Optional[int] = None

    def start_server(self, apk_path: str, port: int, timeout: float = 180.0) -> bool:
        """Start GDA server for the given APK."""
        apk_path = str(Path(apk_path).resolve())

        if not self.gda_exe.exists():
            raise FileNotFoundError(f"GDA.exe not found: {self.gda_exe}")
        if not Path(apk_path).exists():
            raise FileNotFoundError(f"APK not found: {apk_path}")

        # Kill any existing process on same port
        self._kill_port(port)

        try:
            self.process = subprocess.Popen(
                [str(self.gda_exe), "-sv", apk_path, str(port)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )
        except Exception as exc:
            raise RuntimeError(f"Failed to start GDA server: {exc}") from exc

        self.port = port

        # Wait for server to be ready
        if not self._wait_for_server(port, timeout=timeout):
            self._read_stderr()
            self.stop_server()
            raise RuntimeError("GDA server failed to start (timeout)")

        return True

    @staticmethod
    def _kill_port(port: int):
        """Try to kill any process using the port (Windows)."""
        if os.name != "nt":
            return
        try:
            subprocess.run(
                f"netstat -ano | findstr :{port}",
                shell=True,
                capture_output=True,
                timeout=5
            )
        except Exception:
            pass

    def _wait_for_server(self, port: int, timeout: float) -> bool:
        """Wait for server to start accepting connections."""
        start = time.time()
        while time.time() - start < timeout:
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=1):
                    return True
            except OSError:
                time.sleep(0.5)
        return False

    def _read_stderr(self) -> str:
        """Read and return stderr output."""
        if not self.process or not self.process.stderr:
            return ""
        try:
            import select
            if select.select([self.process.stderr], [], [], 0.1)[0]:
                return decode_text_bytes(self.process.stderr.read())
        except Exception:
            pass
        return ""

    def stop_server(self):
        """Stop the GDA server."""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            except Exception:
                pass
            self.process = None
        self.port = None


def suggest_port(apk_path: str) -> int:
    """Suggest a port based on APK path hash."""
    hash_val = sum(bytearray(str(Path(apk_path).resolve()).encode("utf-8")))
    return DEFAULT_PORT_BASE + (hash_val % (DEFAULT_PORT_MAX - DEFAULT_PORT_BASE + 1))


def list_commands():
    """Print available GDA commands."""
    print("GDA server commands (no parameters):")
    print("-" * 60)
    for cmd in GDA_COMMANDS:
        print(f"  {cmd}")
    print("-" * 60)
    print("\nParametric commands (require arguments):")
    for cmd in GDA_PARAMETRIC_COMMANDS:
        print(f"  {cmd}")
    print("-" * 60)
    print("\nPresets:")
    for name, cmds in PRESETS.items():
        print(f"  {name:15}  -> {' '.join(cmds)}")


def run_analysis(apk_file: str, commands: list, gda_exe: Path, port: int = None, timeout: float = 60.0) -> dict:
    """
    Run GDA analysis on an APK.
    Starts server once, executes all commands, stops server once.

    Args:
        apk_file: Path to APK
        commands: List of GDA commands to run
        gda_exe: Path to GDA.exe
        port: Port to use (auto-suggested if not provided)
        timeout: Socket timeout

    Returns:
        Dict mapping command to output
    """
    apk_path = Path(apk_file).resolve()

    # Suggest port if not provided
    if port is None:
        port = suggest_port(str(apk_path))

    # Start server (once)
    manager = GDAServerManager(gda_exe)
    print(f"Starting GDA server on port {port}...")
    manager.start_server(str(apk_path), port, timeout=180.0)

    # Connect client
    client = GDASocketClient(port=port, timeout=timeout)
    if not client.connect():
        manager.stop_server()
        raise RuntimeError("Cannot connect to GDA server")

    # Run commands (all on same server connection)
    results = {}
    for cmd in commands:
        print(f"Executing: {cmd}")
        output = client.execute(cmd)
        results[cmd] = output

        # Show preview
        lines = output.strip().split("\n")
        preview = "\n".join(lines[:5])
        if len(lines) > 5:
            preview += f"\n... ({len(lines) - 5} more lines)"
        print(f"  -> {preview[:200]}")
        print()

    # Cleanup (once)
    client.disconnect()
    manager.stop_server()

    return results


def main():
    parser = argparse.ArgumentParser(
        description="GDA.exe Socket-based Analysis Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("apk_file", nargs="?", help="Path to APK file")
    parser.add_argument("commands", nargs="*", help="GDA commands to run")
    parser.add_argument("--gda", default=str(DEFAULT_GDA_EXE), help="Path to GDA.exe")
    parser.add_argument("--port", type=int, help="Server port (auto-selected if not specified)")
    parser.add_argument("--timeout", type=float, default=60.0, help="Socket timeout in seconds")
    parser.add_argument("--output", "-o", help="Output directory for results")
    parser.add_argument("--list", action="store_true", help="List available commands")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Use analysis preset")

    args = parser.parse_args()

    # Handle --list
    if args.list:
        list_commands()
        return 0

    # Validate APK is provided for other operations
    if not args.apk_file:
        print("[Error] APK file is required", file=sys.stderr)
        parser.print_help()
        return 1

    apk_path = Path(args.apk_file).resolve()

    # Validate APK
    if not apk_path.exists():
        print(f"[Error] APK not found: {apk_path}", file=sys.stderr)
        return 1

    # Validate GDA
    gda_path = Path(args.gda).resolve()
    if not gda_path.exists():
        print(f"[Error] GDA.exe not found: {gda_path}", file=sys.stderr)
        return 1

    # Determine commands
    if args.preset:
        commands = PRESETS[args.preset]
    elif args.commands:
        commands = args.commands
    else:
        commands = PRESETS["basic"]

    # Run analysis
    print(f"\n=== GDA Analysis ===")
    print(f"APK: {apk_path}")
    print(f"GDA: {gda_path}")
    print(f"Port: {args.port or 'auto'}")
    print(f"Commands: {commands}")
    print()

    try:
        results = run_analysis(
            str(apk_path),
            commands,
            gda_path,
            port=args.port,
            timeout=args.timeout
        )

        # Save to output directory if specified
        if args.output:
            output_dir = Path(args.output)
            output_dir.mkdir(parents=True, exist_ok=True)

            for cmd, output in results.items():
                # Sanitize command for filename
                safe_cmd = cmd.replace(" ", "_").replace("@", "_").replace("-", "_")
                output_file = output_dir / f"{apk_path.stem}_{safe_cmd}.txt"
                output_file.write_text(output, encoding="utf-8")
                print(f"Saved: {output_file}")

        print(f"\n=== Analysis Complete ===")
        return 0

    except Exception as e:
        print(f"[Error] {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
