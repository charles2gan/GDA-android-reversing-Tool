import sys
import socket
import struct
import locale

HOST = '127.0.0.1'
PORT = 8888

def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <command>")
        sys.exit(1)

    command = sys.argv[1] + '\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except socket.error as e:
        print(f"Connection error: {e}")
        sys.exit(1)

    sock.sendall(command.encode())

    len_data = sock.recv(4)
    if len(len_data) < 4:
        print("Error: Incomplete length received")
        sock.close()
        sys.exit(1)

    resp_len = struct.unpack('!I', len_data)[0]
    resp_data = b''
    while len(resp_data) < resp_len:
        chunk = sock.recv(resp_len - len(resp_data))
        if not chunk:
            break
        resp_data += chunk

    if len(resp_data) != resp_len:
        print("Warning: Incomplete response received")

    encoding = locale.getpreferredencoding()
    try:
        print(resp_data.decode(encoding), end='')
    except UnicodeDecodeError:
        print(resp_data.decode(encoding, errors='replace'), end='')

    sock.close()

if __name__ == "__main__":
    main()