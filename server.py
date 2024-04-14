import socket
from _thread import *
from board import Board

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server = read("ip_address","r").strip()
# Địa chỉ IP của máy tính cá nhân
server = "192.168.5.143"

port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

bo = Board(8,8)

currentID = "w"

def threaded_client(conn):
    global currentID, pos
    conn.send(str.encode(bo), str.encode(currentID))
    currentID = "b"
    reply = ''

    while True:
        try: 
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Client Left!"))
                break
            else:
                print("Received: " + reply)

                if reply.count("w") == 1:
                    nid = "b"
                else:
                    nid = "w"

                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection closed!")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ")

    start_new_thread(threaded_client, (conn,))