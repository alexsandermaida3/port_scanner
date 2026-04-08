import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    try:
        result = scanner.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        scanner.close()
    except KeyboardInterrupt:
        print("\nScan interrupted.")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    except socket.error:
        print("Could not connect to server.")
        exit()

def scan(ip):
    print(f"Scanning target: {ip}")
    for port in range(1, 1025):  # first 1024 ports
        scan_port(ip, port)

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan(target)
