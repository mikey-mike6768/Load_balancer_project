
# Load Balancer Project

This project implements a simple HTTP load balancer that distributes incoming traffic across multiple backend servers. The load balancer ensures optimal resource usage, improves fault tolerance, and enhances the system's scalability by forwarding HTTP requests to backend servers in a round-robin or other balancing algorithms.

## Features

- **HTTP Load Balancing**: Distributes HTTP requests across multiple backend servers.
- **Health Checker**: Monitors backend server health to ensure only live servers receive traffic.
- **Scalability**: Easily add or remove backend servers as needed.
- **Error Handling**: Detects server downtime and reroutes traffic to live servers.
  
## File Overview

- `.gitignore`: Specifies files and directories to be ignored by version control.
- `LICENSE`: License information for the project (MIT License).
- `README.md`: This documentation file explaining the project structure and usage.
- `backend_server.py`: A simple backend server implementation that listens for incoming HTTP requests.
- `health_checker.py`: Monitors the health status of backend servers to ensure traffic is routed to active servers.
- `lb.py`: The core load balancer logic. It listens for incoming HTTP requests and distributes them to the backend servers based on the load balancing strategy.
- `requirements.txt`: Lists the dependencies required to run the project.

## Requirements

This project requires Python 3.x and a few external libraries, which are listed in the `requirements.txt` file. To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Start Backend Servers

Before starting the load balancer, you'll need to launch multiple backend servers. Each backend server listens on a different port. You can start backend servers using the `backend_server.py` script. For example:

```bash
python backend_server.py --port 8081
python backend_server.py --port 8082
```

These commands will start backend servers listening on ports 8081 and 8082.

### Step 2: Start the Load Balancer

After starting the backend servers, you can start the load balancer using the `lb.py` script. The load balancer will listen for incoming traffic on a specified port (default is 8080) and distribute the requests to the available backend servers:

```bash
python lb.py --port 8080
```

This will start the load balancer on port 8080. It will forward requests to the backend servers defined in the `lb.py` configuration.

### Step 3: Health Checking

The `health_checker.py` script ensures that the backend servers are live and capable of handling requests. It periodically checks the status of the backend servers and removes unhealthy servers from the rotation.

To run the health checker:

```bash
python health_checker.py
```

The health checker will monitor the backend servers defined in the configuration and log any status changes.

### Load Balancing Strategy

The load balancer distributes traffic using a round-robin strategy, but it can be customized to use other algorithms such as:
- **Round Robin**
- **Least Connections**
- **Random Selection**

To modify the load balancing algorithm, you can update the logic in `lb.py`.

## Contributing

Contributions are welcome! If you'd like to add a feature or report an issue, feel free to open a pull request or submit an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Future Improvements

- Implement support for HTTPS traffic.
- Add logging and analytics to track server performance and request distribution.
- Improve fault tolerance by introducing automatic scaling of backend servers.
