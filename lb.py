import socket
import threading
import time
import requests
from health_checker import check_health

# List of backend servers (IP, port)
BACKEND_SERVERS = [('127.0.0.1', 8081), ('127.0.0.1', 8082)]

# Server health status
server_status = {server: True for server in BACKEND_SERVERS}
current_server = 0  # Used for round-robin scheduling
lock = threading.Lock()  # Ensure thread safety for current_server

def handle_client(client_socket):
    global current_server

    # Use round-robin to select a server
    with lock:
        while True:
            backend_server = BACKEND_SERVERS[current_server]
            if server_status[backend_server]:
                break
            current_server = (current_server + 1) % len(BACKEND_SERVERS)

        backend_ip, backend_port = backend_server
        current_server = (current_server + 1) % len(BACKEND_SERVERS)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
            backend_socket.connect((backend_ip, backend_port))
            client_request = client_socket.recv(1024)
            
            # Log the client request
            print(f"[*] Forwarding client request to {backend_ip}:{backend_port}")
            print(f"[*] Client request: {client_request.decode('utf-8')}")
            backend_socket.sendall(client_request)

            # Get the response from the backend server in chunks
            backend_response = b""
            while True:
                chunk = backend_socket.recv(4096)
                if not chunk:
                    break
                backend_response += chunk

            if backend_response:
                print(f"[*] Response from {backend_ip}:{backend_port}: {backend_response.decode('utf-8')}")
                client_socket.sendall(backend_response)
            else:
                print(f"[!] No response from {backend_ip}:{backend_port}")

    except Exception as e:
        print(f"Error communicating with backend server {backend_ip}:{backend_port} - {e}")
    finally:
        client_socket.close()

def start_load_balancer():
    load_balancer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    load_balancer_socket.bind(('0.0.0.0', 8080))  # Using port 8080 instead of 80
    load_balancer_socket.listen(5)
    print("[*] Load balancer started on port 8080")

    while True:
        client_socket, _ = load_balancer_socket.accept()
        print("[*] Incoming client request")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    threading.Thread(target=check_health, args=(BACKEND_SERVERS, server_status)).start()
    start_load_balancer()
