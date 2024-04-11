# Socket programming example: custom server-side configuration.
import socket

def initialize_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    # Port for your service (ensure it's above 1024 because below it requires)
    port = 999

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    print(f"Server listening on port {port}...")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection")
        msg = 'Welcome' + "\r\n"  # Modified message
        client_socket.send(msg.encode('ascii'))
        client_socket.close()

if __name__ == '__main__':
    initialize_server()
