import time
import requests

def check_health(servers, server_status, check_interval=10):
    while True:
        for server in servers:
            ip, port = server
            url = f"http://{ip}:{port}/"  # Health check URL
            try:
                # Log the health check attempt
                print(f"[*] Checking health for {server}")
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    server_status[server] = True
                    print(f"[*] {server} is healthy")
                else:
                    server_status[server] = False
                    print(f"[!] {server} failed health check")
            except requests.RequestException as e:
                server_status[server] = False
                print(f"[!] {server} is offline: {e}")

        time.sleep(check_interval)
