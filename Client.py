import socket
import argparse
import os

# Define banner
CLIENT_BANNER = """
*****************************************
*          Netcat Client               *
*****************************************
"""

def send_file(server_socket, filename):
    with open(filename, 'rb') as file:
        server_socket.send(f"FILE:{os.path.basename(filename)}".encode())
        while True:
            data = file.read(4096)
            if not data:
                break
            server_socket.send(data)
    print(f"File {filename} sent successfully")

def start_netcat_client(host, port, protocol, timeout, filename=None):
    try:
        print(CLIENT_BANNER)  # Display the banner when the client starts

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM)
        client_socket.settimeout(timeout)
        client_socket.connect((host, port))

        if filename:
            send_file(client_socket, filename)
        else:
            while True:
                message = input("Enter message: ")
                if not message:
                    break
                client_socket.send(message.encode())

    except KeyboardInterrupt:
        print("\nClosing connection...")
        client_socket.close()

def main():
    parser = argparse.ArgumentParser(description="Netcat client implementation in Python")
    parser.add_argument('host', help="Server host")
    parser.add_argument('port', help="Server port", type=int)
    parser.add_argument('--protocol', help="Protocol (tcp/udp)", choices=["tcp", "udp"], default="tcp")
    parser.add_argument('--timeout', help="Connection timeout", type=int, default=None)
    parser.add_argument('--file', help="File to send")
    args = parser.parse_args()

    host = args.host
    port = args.port
    protocol = args.protocol
    timeout = args.timeout
    filename = args.file

    start_netcat_client(host, port, protocol, timeout, filename)

if __name__ == "__main__":
    main()
