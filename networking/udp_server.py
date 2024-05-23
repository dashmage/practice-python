from socket import AF_INET, SOCK_DGRAM, socket

HOST = ''  # all available interfaces
PORT = 12000  # arbritary non-priveleged port

# AF_INET: address family is ipv4
# SOCK_DGRAM: socket type is UDP
with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("The server is ready to receive")
    while True:
        # client_address is a tuple with host, port
        msg, client_address = s.recvfrom(1024)
        modified_msg = msg.decode().upper()
        s.sendto(modified_msg.encode(), client_address)
