__author__ = "CISCO"

import socket
import select
import sys


def refresh():
    sys.stdout.write("<YOU>")
    sys.stdout.flush()


if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    # creating socket
    csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        csocket.connect((host, port))
    except:
        print("can not to connect")
        sys.exit()
    print("socket connected to the host")
    refresh()
    while True:
        socket_list = [sys.stdin, csocket]
        readable_socket, writeable_socket, err_signal = select.select(socket_list, [], [])
        for sock in readable_socket :
            # receiving message
            if sock == csocket :
                data = sock.recv(4096)
                if not data:
                    print("the client disconnected")
                    sys.exit()
                if data:
                    sys.stdout.write()
                    refresh()







            # sending message
            else:
                message = sys.stdin.readline()
                csocket.send(message)
                refresh()





