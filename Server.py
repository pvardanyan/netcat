import socket
import argparse
import threading
import os

# Define banners
TCP_BANNER = """
*****************************************
*          TCP Netcat Server           *
*****************************************
"""

UDP_BANNER = """
*****************************************
*          UDP Netcat Server           *
*****************************************
"""

def handle_client(client_socket, address):
    print(f"Connected to {address[0]}:{address[1]}")

    while True:
        data = client_socket.recv(4096)
        if not data:
            print(f"Disconnected from {address[0]}:{address[1]}")
            break
        print(f"Received from {address[0]}:{address[1]}: {data.decode()}")

        # Check if the received data is a file transfer request
        if data.decode().startswith("FILE:"):
            filename = data.decode().split(':')[1]
            receive_file(client_socket, filename)

def receive_file(client_socket, filename):
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            file.write(data)
    print(f"File {filename} received successfully")

def start_netcat_server(host, port, protocol, timeout):
    try:
        # Selecting banner based on protocol
        if protocol == "tcp":
            print(TCP_BANNER)
        elif protocol == "udp":
            print(UDP_BANNER)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port} ({protocol.upper()})...")

        while True:
            client_socket, address = server_socket.accept()
            client_socket.settimeout(timeout)
            client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
            client_handler.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server_socket.close()

def main():
    parser = argparse.ArgumentParser(description="Netcat server implementation in Python")
    parser.add_argument('--host', help="Server host", default="0.0.0.0")
    parser.add_argument('--port', help="Server port", type=int, default=12345)
    parser.add_argument('--protocol', help="Protocol (tcp/udp)", choices=["tcp", "udp"], default="tcp")
    parser.add_argument('--timeout', help="Connection timeout", type=int, default=None)
    args = parser.parse_args()

    host = args.host
    port = args.port
    protocol = args.protocol
    timeout = args.timeout

    start_netcat_server(host, port, protocol, timeout)

if __name__ == "__main__":
    main()
