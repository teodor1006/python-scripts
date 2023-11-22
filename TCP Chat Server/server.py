import socket
import threading

def handle_client(client_sock, addr):
    print(f"Accepted connection from {addr}")
    client_sock.send(bytes("Welcome to the chat server!\n", "utf-8"))

    while True:
        data = client_sock.recv(1024)
        if not data:
            break

        message = f"[{addr[0]}:{addr[1]}] {data.decode('utf-8')}"
        print(message)
        broadcast(message)

    client_sock.close()
    print(f"Connection from {addr} closed")
    

def broadcast(message):
    for client in clients:
        client.send(bytes(message, "utf-8"))

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("0.0.0.0", 1234))
server_sock.listen(5)
print("Server listening on port 1234")

clients = []

try:
    while True:
        client_sock, addr = server_sock.accept()
        clients.append(client_sock)

        client_handler = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_handler.start()

except KeyboardInterrupt:
    print("Server shutting down.")

finally:
    for client in clients:
        client.close()

    server_sock.close()        

