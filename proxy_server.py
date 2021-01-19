import socket, sys, time

# create tcp socket
def create_tcp_socket():
    print("Creating socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("Failed to create socket")
        sys.exit()
    print("Created socket")

    return s

# get host information
def get_remote_ip(host):
    print(f"Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting...")
        sys.exit()
    print(f"IP address of {host} is {remote_ip}")
    
    return remote_ip

# send data to server
def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("Sending failed")
        sys.exit()
    print("Sent successfully")

def main():
    # connect to google
    try:
        # define address info, payload, and buffer size
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096

        # make the socket, get the ip, and connect
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip , port))
        print (f'Socket connected to {host} on ip {remote_ip}')
        
        # send the data and shutdown
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        # continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                 break
            full_data += data
        print("Recieved data from Google")
    
    except Exception as e:
        print(e)
    finally:
        # always close at the end!
        s.close()

    # start proxy server
    # define address & buffer size
    HOST = ""
    PORT = 8001
    BUFFER_SIZE = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)
        print(f"Started proxy server, listening on port {PORT}")
        
        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            # print connections to the server socket 
            print("Connected by", addr)
            # recieve data, wait a bit, then send it back
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()