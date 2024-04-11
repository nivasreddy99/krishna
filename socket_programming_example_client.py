# Socket programming example: client side config.
import socket

def socket_example_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    # Port for the service, the same as used by the server
    port = 999

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    # Receive no more than 1024 bytes
    msg = client_socket.recv(1024)

    client_socket.close()
    print("Client connected!")
    print(msg.decode('ascii'))

if __name__ == '__main__':
    socket_example_client()
