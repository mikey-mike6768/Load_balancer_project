
# Build Your Own Load Balancer

## Overview
This project implements a simple application-layer load balancer that distributes HTTP requests between two or more backend servers using a round-robin scheduling algorithm.

## Features
- Load balancing between multiple servers
- Round-robin request distribution
- Health checks on backend servers
- Automatic failover when a server goes offline

## Files
- `lb.py`: Load balancer logic that routes requests.
- `health_checker.py`: Periodically checks the health of backend servers.
- `backend_server.py`: A mock backend server that responds to HTTP requests.

## Setup Instructions

1. Clone the project:
   ```
   git clone <your-repo-url>
   cd load_balancer_project
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the backend servers:
   ```
   python3 backend_server.py 8080
   python3 backend_server.py 8081
   ```

4. Run the load balancer:
   ```
   sudo python3 lb.py
   ```

5. Test the setup:
   ```
   curl http://localhost/
   ```

You should see responses alternate between servers on ports 8080 and 8081. If a server goes offline, the load balancer will stop sending traffic to it.

## Further Extensions
- Add logging for better debugging and analysis.
- Implement more advanced load-balancing algorithms (e.g., least connections).
- Improve health check mechanisms (e.g., using thresholds before marking a server as unhealthy).
