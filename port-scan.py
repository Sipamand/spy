import socket


target_host = "google.com"
start_port = 50
end_port = 5060


def scan_port(host, port):
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.settimeout(1)
            
            
            s.connect((host, port))
            

            print(f"Port {port} is open")
    except:
    
        print(f"Port {port} is closed")

for port in range(start_port, end_port + 1):
    scan_port(target_host, port)
