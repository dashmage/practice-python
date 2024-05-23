from socket import socket, AF_INET, SOCK_DGRAM

HOST = "localhost"
PORT = 12000  # same port used by server
with socket(AF_INET, SOCK_DGRAM) as s:
    while True:
        msg = input("Enter message to send to server: ")
        if msg == 'q':
            print("bye")
            s.close()
            break
        s.sendto(msg.encode(), (HOST, PORT))
        modified_msg, server_address = s.recvfrom(1024)
        print(f"Respose: {modified_msg.decode()}")
