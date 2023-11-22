import socket
import threading

def receive_messages(client_sock):
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

def send_messages(client_sock):
    while True:
        message = input("Enter your message: ")
        client_sock.send(bytes(message, 'utf-8'))

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(("127.0.0.1", 1234))

recv_thread = threading.Thread(target=receive_messages, args=(client_sock,))
send_thread = threading.Thread(target=send_messages, args=(client_sock,))

recv_thread.start()
send_thread.start()

recv_thread.join()
send_thread.join()

client_sock.close()