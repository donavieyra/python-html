import socket

SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 8000       # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f'Listening on port {SERVER_PORT}...')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print(f"Received request from {client_address}:\n{request}")

    try:
        with open('index.html', 'r') as fin:
            content = fin.read()
        response = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
    except FileNotFoundError:
        content = "<h1>404 Not Found</h1>"
        response = 'HTTP/1.0 404 NOT FOUND\r\nContent-Type: text/html\r\n\r\n' + content

    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()
