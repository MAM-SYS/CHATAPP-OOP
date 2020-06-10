__author__ = "mastermind"

import socket
import sys
import select



# creating socket

def broadcast_data(sock, message):
    for socket in client_list:
        if socket != sock and socket != server_socket:
            try:
                socket.send(message)
            except:
                socket.close()
                client_list.remove(socket)


if __name__ == "__main__":
    client_list = []

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("not created")
        sys.exit()
    print("socket created")

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket

    port = 5000
    try:
        server_socket.bind(("0.0.0.0", port))
    except:
        print("not bound")
        sys.exit()
    print("socket bound")
    # listening
    server_socket.listen(10)
    print("socket is listening...")

    client_list.append(server_socket)
    # accepting incoming
    while True:
        readable, writeable, err_signal = select.select(client_list, [], [])
        for sock in readable:

            if sock == server_socket:
                conn, add = server_socket.accept()
                client_list.append(conn)
                print("client (%s,%s) connected" % add)
            broadcast_data(sock, "client [%s,%s] entered room" % add)

        else:
            try:
                data = sock.recv(4096)
                if data:
                    broadcast_data(sock, "<" + sock.getpeername() + ">" + data)
            except:
                broadcast_data(sock, "the client with address:" + sock.getpeername() + "is offline")
                sock.close()
                client_list.remove(sock)
                continue
    server_socket.close()
