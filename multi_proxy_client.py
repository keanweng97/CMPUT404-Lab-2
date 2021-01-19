import socket
from multiprocessing import Pool

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

def connect(address):
    buffer_size = 4096
    # make the socket and connect
    s = create_tcp_socket()

    s.connect(address)
    print (f'Socket connected to {address[0]}:{address[1]}')

    s.shutdown(socket.SHUT_WR)

    # continue accepting data until no more left
    full_data = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
                break
        full_data += data
    print(full_data)

def main():
    # define address info, payload, and buffer size
    host = 'localhost'
    port = 8001

    address = [(host, port)]
    # establish 10 different connections
    with Pool() as p:
        p.map(connect, address * 10)

if __name__ == "__main__":
    main()