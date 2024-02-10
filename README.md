# Netcat Implementation in Python

This project provides a simple implementation of the Netcat tool in Python, allowing users to establish both client and server connections for TCP and UDP protocols.

## Usage

### Server

To start the Netcat server, run the following command:

```bash
python netcat_server.py [--host HOST] [--port PORT] [--protocol {tcp,udp}] [--timeout TIMEOUT]
```

--host: Server host (default is "0.0.0.0").
--port: Server port (default is 12345).
--protocol: Protocol to use (choose between "tcp" or "udp", default is "tcp").
--timeout: Connection timeout in seconds (default is None).

### Client

To connect to the Netcat server as a client, run the following command:

```bash
python netcat_client.py HOST PORT [--protocol {tcp,udp}] [--timeout TIMEOUT] [--file FILE]
```

HOST: Server host.
PORT: Server port.
--protocol: Protocol to use (choose between "tcp" or "udp", default is "tcp").
--timeout: Connection timeout in seconds (default is None).
--file: File to send to the server (optional).


### Example
Start the server:
```bash
python netcat_server.py --port 12345
```

Connect to the server as a client:
```bash
python netcat_client.py localhost 12345
```
