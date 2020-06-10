__author__ = "CISCO"
import select, sys, socket


class client():

 def __init__(self, name, host ="0.0.0.0", port="8000"):
    self.name = name
    self.host = host
    self.port = int(port)
    self.buffer_size = 4096
    try:
        self.c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
        print("socket not created...")
        sys.exit()
    try:
        self.c_socket.connect((self.host,self.port))
    except:
        print("socket not connected...")
    self.flush()
    self.c_socket.send('<'+self.name+'>: '+sys.argv[2]+':'+sys.argv[3])


 def flush(self) :
    sys.stdout.write('<'+self.name+'>\n')
    sys.stdout.flush()


 def chat_method(self):
    socket_list = [sys.stdin, self.c_socket]
    while True:
        readable, writeable, err_signal = select.select(socket_list, [],[])
        for sock in readable :
            if sock == self.c_socket :
                data = sock.recv(self.buffer_size)
                if data :
                    sys.stdout.write(data)
                    self.flush()
                else :
                    sys.stdout.write("no data...")
            else :
                message = sys.stdin.readline()
                self.c_socket.send(message)
                self.flush()

if __name__ == "__main__" :
	client_name = sys.argv[1]
	host = sys.argv[2]
	port = sys.argv[3]

	client = client(client_name, host, port)
	client.chat_method()





