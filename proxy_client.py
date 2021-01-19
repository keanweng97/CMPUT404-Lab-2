import socket

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

def main():
    # define address info, payload, and buffer size
    host = '127.0.0.1'
    port = 8001
    buffer_size = 4096

    # make the socket and connect
    s = create_tcp_socket()

    s.connect((host , port))
    print (f'Socket connected to {host}:{port}')

    s.shutdown(socket.SHUT_WR)

    # continue accepting data until no more left
    full_data = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
                break
        full_data += data
    print(full_data)

if __name__ == "__main__":
    main()