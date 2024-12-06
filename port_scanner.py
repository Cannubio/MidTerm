import socket

def port_scanner(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}")
    open_ports = []  # List to store open ports
    
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")  # Debugging output
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Timeout for each connection
            
            # Attempt to connect to the port
            result = s.connect_ex((host, port))  
            if result == 0:
                open_ports.append(port)
                print(f"Port {port}: OPEN")  # Print if port is open
            s.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")
    
    print("\nScan complete.")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    # User inputs for host and port range
    host = input("Enter host to scan (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port (e.g., 20): "))
    end_port = int(input("Enter end port (e.g., 80): "))
    
    # Call the port scanner function
    port_scanner(host, start_port, end_port)
