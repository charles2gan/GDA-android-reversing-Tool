import subprocess
import socket
import time
import threading
import json
import os
from typing import Dict, Any, Optional

class GDAServerManager:
    """Manage the lifecycle of the GDA server process"""
    def __init__(self, gda_exe_path: str = "gda.exe"):
        self.gda_exe = gda_exe_path
        self.process: Optional[subprocess.Popen] = None
        self.apk_path: Optional[str] = None
        self.port: int = 8888
        self.lock = threading.Lock()

    def start_server(self, apk_path: str, port: int = 8888) -> bool:
        """Start the GDA server, wait for the port to be ready, return success"""
        with self.lock:
            if self.is_running():
                # If a server is already running, check if it's the same APK and port
                if self.apk_path == apk_path and self.port == port:
                    return True
                else:
                    self.stop_server()  # Stop old server if conflict

            if not os.path.exists(apk_path):
                raise FileNotFoundError(f"APK file not found: {apk_path}")

            self.apk_path = apk_path
            self.port = port

            # Start process, do not wait for it to exit
            try:
                self.process = subprocess.Popen(
                    [self.gda_exe, "-sv", apk_path, str(port)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )
            except Exception as e:
                raise RuntimeError(f"Failed to start GDA server: {e}")

            # Wait for the port to be listening
            return self._wait_for_server(port, timeout=1000)

    def _wait_for_server(self, port: int, timeout: float = 10) -> bool:
        """Try to connect to the specified port until success or timeout"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=1):
                    return True
            except (socket.error, ConnectionRefusedError):
                time.sleep(0.5)
        return False

    def is_running(self) -> bool:
        """Check if the server process is still running"""
        if self.process is None:
            return False
        return self.process.poll() is None

    def stop_server(self):
        """Stop the server process"""
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
        self.process = None
        self.apk_path = None
        self.port = 8888

    def get_connection_info(self):
        """Return current server information"""
        if not self.is_running():
            raise RuntimeError("GDA server is not running")
        return self.apk_path, self.port


class GDAClient:
    """Connect to GDA server and execute commands"""
    def __init__(self, host: str = "127.0.0.1", port: int = 8888):
        self.host = host
        self.port = port
        self._socket = None
        self._lock = threading.Lock()

    def _connect(self):
        """Establish a TCP connection (new connection per command, simple and reliable)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        return sock

    def execute(self, cmd: str) -> str:
        """Send a command and return the full response (assuming server separates responses with newline and closes connection)"""
        with self._lock:
            try:
                with self._connect() as sock:
                    sock.sendall((cmd + "\n").encode("utf-8"))
                    response = b""
                    while True:
                        data = sock.recv(4096)
                        if not data:
                            break
                        response += data
                    return response.decode("utf-8", errors="replace")
            except Exception as e:
                return f"Error: {str(e)}"


# ========== Skill command construction logic (same as before) ==========
def build_command(skill_name: str, arguments: Dict[str, Any]) -> str:
    """Construct the subcmd command string based on skill name and arguments"""
    cmd_map = {
        "apk_help": "help",
        "apk_set_output": "set -o",
        "apk_exit": "exit",
        "apk_axml": "axml",
        "apk_binfo": "binfo",
        "apk_pname": "pname",
        "apk_permission": "permission",
        "apk_header": "header",
        "apk_attsf": "attsf",
        "apk_packer": "packer",
        "apk_cert": "cert",
        "apk_appstr": "appstr",
        "apk_malscan": "malscan",
        "apk_sensinf": "sensinf",
        "apk_interface": "interface",
        "apk_uri": "uri",
        "apk_native": "native",
        "apk_api": "api",
        "apk_listm": "listm",
        "apk_sclass": "sclass",
        "apk_pclass": "pclass",
        "apk_dasm": "dasm",
        "apk_dec": "dec",
        "apk_find": "find",
        "apk_xref": "xref",
        "apk_start_server": "start_server",   # Special skill, not sent to GDA
        "apk_stop_server": "stop_server",     # Special skill
    }

    subcmd = cmd_map.get(skill_name)
    if not subcmd:
        raise ValueError(f"Unknown skill: {skill_name}")

    # These skills are handled by the local manager and are not sent to GDA
    if skill_name in ("apk_start_server", "apk_stop_server"):
        return subcmd

    if skill_name == "apk_set_output":
        if "file" not in arguments:
            raise ValueError("Missing required argument 'file'")
        return f"{subcmd} {arguments['file']}"
    elif skill_name == "apk_header":
        if "n" not in arguments:
            raise ValueError("Missing required argument 'n'")
        return f"{subcmd} {arguments['n']}"
    elif skill_name == "apk_listm":
        if "cname" not in arguments:
            raise ValueError("Missing required argument 'cname'")
        return f"{subcmd} {arguments['cname']}"
    elif skill_name in ("apk_sclass", "apk_pclass"):
        if "cidx" not in arguments:
            raise ValueError("Missing required argument 'cidx'")
        return f"{subcmd} {arguments['cidx']}"
    elif skill_name == "apk_dasm":
        if "method_ref" not in arguments:
            raise ValueError("Missing required argument 'method_ref'")
        return f"{subcmd} {arguments['method_ref']}"
    elif skill_name == "apk_dec":
        if "target" not in arguments:
            raise ValueError("Missing required argument 'target'")
        return f"{subcmd} {arguments['target']}"
    elif skill_name == "apk_find":
        opt_map = {
            "class": "-c",
            "class_with_package": "-C",
            "method": "-m",
            "method_with_package": "-M",
            "field": "-d",
            "api_method": "-i",
            "string": "-s",
            "all": "-a",
        }
        stype = arguments.get("search_type")
        if not stype or stype not in opt_map:
            raise ValueError(f"Invalid search_type: {stype}")
        name = arguments.get("name")
        if not name:
            raise ValueError("Missing required argument 'name'")
        return f"{subcmd} {opt_map[stype]} {name}"
    elif skill_name == "apk_xref":
        opt_map = {
            "class": "-c",
            "method": "-m",
            "field": "-f",
            "string": "-s",
            "resource": "-r",
            "all": "-a",
        }
        xtype = arguments.get("xref_type")
        if not xtype or xtype not in opt_map:
            raise ValueError(f"Invalid xref_type: {xtype}")
        name = arguments.get("name")
        if not name:
            raise ValueError("Missing required argument 'name'")
        return f"{subcmd} {opt_map[xtype]} {name}"
    else:
        return subcmd


# ========== Main execution logic ==========
class GDASkillExecutor:
    """Integrate server management and skill execution"""
    def __init__(self, gda_exe_path: str = "gda.exe"):
        self.manager = GDAServerManager(gda_exe_path)
        self.client: Optional[GDAClient] = None

    def execute_skill(self, skill_name: str, arguments: Dict[str, Any]) -> str:
        """Execute a single skill, automatically manage server state"""
        # Handle special skills
        if skill_name == "apk_start_server":
            apk_file = arguments.get("apk_file")
            if not apk_file:
                return "Error: Missing required argument 'apk_file'"
            port = arguments.get("port", 8888)
            try:
                success = self.manager.start_server(apk_file, port)
                if success:
                    # Create client connection
                    self.client = GDAClient(port=port)
                    return f"GDA server started successfully on port {port} with APK {apk_file}"
                else:
                    return f"Failed to start GDA server (timeout)."
            except Exception as e:
                return f"Error starting server: {e}"

        elif skill_name == "apk_stop_server":
            self.manager.stop_server()
            self.client = None
            return "GDA server stopped."

        # Other skills require the server to be running
        if not self.manager.is_running():
            return "Error: GDA server is not running. Please use apk_start_server first."

        if self.client is None:
            # Recreate client (port may have changed)
            _, port = self.manager.get_connection_info()
            self.client = GDAClient(port=port)

        try:
            cmd = build_command(skill_name, arguments)
            if cmd in ("start_server", "stop_server"):  # Safety guard
                return "Invalid command"
            print(f"[CMD] {cmd}")
            return self.client.execute(cmd)
        except Exception as e:
            return f"Skill execution failed: {e}"


# ========== Integration with large model function calling ==========
def handle_function_call(executor: GDASkillExecutor, function_call: Dict[str, Any]) -> str:
    """Handle function calls from the large model"""
    name = function_call.get("name")
    args = function_call.get("arguments", {})
    return executor.execute_skill(name, args)


# ========== Example usage ==========
if __name__ == "__main__":
    # Create executor (gda.exe needs to be in PATH or specify absolute path)
    executor = GDASkillExecutor(gda_exe_path="gda.exe")  # or "C:/path/to/gda.exe"

    # Simulate a sequence of large model function calls
    calls = [
        {"name": "apk_start_server", "arguments": {"apk_file": "2.apk", "port": 8888}},
        {"name": "apk_binfo", "arguments": {}},
        {"name": "apk_uri", "arguments": {}},
        {"name": "apk_stop_server", "arguments": {}}
    ]

    for call in calls:
        result = handle_function_call(executor, call)
        print(f"\n--- {call['name']} ---")
        print(result)