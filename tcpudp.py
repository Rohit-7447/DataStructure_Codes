#tcp_client.py
import socket
import sys
import os

BUFFER_SIZE = 8192

def send_file(sock, filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist")
        return

    file_size = os.path.getsize(filename)
    name_bytes = os.path.basename(filename).encode()

    try:
        # Send metadata
        sock.sendall(len(name_bytes).to_bytes(4, 'big'))
        sock.sendall(name_bytes)
        sock.sendall(file_size.to_bytes(8, 'big'))

        print(f"Sending '{filename}' ({file_size} bytes)")

        with open(filename, 'rb') as f:
            sent = 0
            while chunk := f.read(BUFFER_SIZE):
                sock.sendall(chunk)
                sent += len(chunk)
                print(f"\rProgress: {(sent * 100) // file_size}%", end='', flush=True)

        print("\nFile sent successfully!")

    except Exception as e:
        print(f"\nError: {e}")

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <server_ip> <port> <filename>")
        return

    ip, port, filename = sys.argv[1], int(sys.argv[2]), sys.argv[3]

    try:
        with socket.create_connection((ip, port)) as sock:
            print(f"Connected to {ip}:{port}")
            send_file(sock, filename)
    except ConnectionRefusedError:
        print(f"Connection refused. Is the server running at {ip}:{port}?")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Connection closed")

if __name__ == "__main__":
    main()


#tcp_server.py
import socket
import sys
import os

BUFFER_SIZE = 8192

def receive_file(sock, addr):
    try:
        name_len = int.from_bytes(sock.recv(4), 'big')
        filename = sock.recv(name_len).decode()
        file_size = int.from_bytes(sock.recv(8), 'big')

        print(f"Receiving '{filename}' ({file_size} bytes) from {addr[0]}")

        with open(f"received_{filename}", 'wb') as f:
            received = 0
            while received < file_size:
                data = sock.recv(min(BUFFER_SIZE, file_size - received))
                if not data:
                    break
                f.write(data)
                received += len(data)
                print(f"\rProgress: {(received * 100) // file_size}%", end='', flush=True)

        print("\nFile received successfully!")

    except Exception as e:
        print(f"\nError: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        return

    try:
        port = int(sys.argv[1])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('0.0.0.0', port))
            server.listen(5)
            print(f"Server listening on port {port}")

            while True:
                client_sock, client_addr = server.accept()
                with client_sock:
                    print(f"Connected: {client_addr[0]}:{client_addr[1]}")
                    receive_file(client_sock, client_addr)
                    print(f"Connection closed: {client_addr[0]}")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    main()



#udp_client.py
import socket
import sys
import os
import struct

BUFFER_SIZE = 4096
TIMEOUT = 1.0
RETRIES = 5

def send_file(sock, addr, filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found")
        return False

    file_size = os.path.getsize(filename)
    name_bytes = os.path.basename(filename).encode()
    metadata = bytes([len(name_bytes)]) + name_bytes + struct.pack("!Q", file_size)

    sock.settimeout(TIMEOUT)

    # Send metadata and wait for ACK
    for attempt in range(RETRIES):
        sock.sendto(metadata, addr)
        try:
            if sock.recvfrom(BUFFER_SIZE)[0] == b"ACK":
                break
        except socket.timeout:
            print(f"Retry {attempt+1}/{RETRIES} - waiting for ACK")
    else:
        print("Connection setup failed")
        return False

    print(f"Sending '{filename}' ({file_size} bytes)")

    with open(filename, "rb") as f:
        seq, sent = 0, 0

        while sent < file_size:
            chunk = f.read(BUFFER_SIZE - 4)
            if not chunk: break

            packet = struct.pack("!I", seq) + chunk
            for attempt in range(RETRIES):
                sock.sendto(packet, addr)
                try:
                    ack = sock.recvfrom(BUFFER_SIZE)[0]
                    if struct.unpack("!I", ack)[0] == seq:
                        break
                except socket.timeout:
                    print(f"\rRetry {attempt+1}/{RETRIES} for packet {seq}", end="")
            else:
                print(f"\nFailed to send packet {seq}")
                return False

            sent += len(chunk)
            seq += 1
            print(f"\rProgress: {sent * 100 // file_size}%", end="", flush=True)

    print("\nFile sent successfully")
    return True

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <server_ip> <port> <filename>")
        return

    ip, port, filename = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            send_file(sock, (ip, port), filename)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()



#udp_server.py
import socket
import sys
import struct

BUFFER_SIZE = 4096

def receive_file(sock):
    metadata, client = sock.recvfrom(BUFFER_SIZE)

    # Parse metadata: filename length, name, and file size
    name_len = metadata[0]
    filename = metadata[1:1+name_len].decode()
    file_size = struct.unpack("!Q", metadata[1+name_len:1+name_len+8])[0]

    print(f"Receiving '{filename}' ({file_size} bytes) from {client[0]}")

    # Send ACK to confirm metadata received
    sock.sendto(b"ACK", client)

    with open(f"received_{filename}", "wb") as f:
        received = 0

        while received < file_size:
            packet, addr = sock.recvfrom(BUFFER_SIZE)
            seq = struct.unpack("!I", packet[:4])[0]
            data = packet[4:]

            f.write(data)
            received += len(data)

            # Send ACK for the received packet
            sock.sendto(struct.pack("!I", seq), addr)

            print(f"\rProgress: {received * 100 // file_size}%", end="", flush=True)

    print("\nFile received successfully.")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        return

    port = int(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('0.0.0.0', port))
        print(f"UDP server listening on port {port}")

        try:
            while True:
                receive_file(sock)
        except KeyboardInterrupt:
            print("\nServer shutting down...")

if __name__ == "__main__":
    main()