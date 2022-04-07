import socket

# write a socket class for a client side socket
class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    
    def connect(self, host, port):
        self.sock.connect((host, port))
    
    def mysend(self, msg):
        print("Starting mysend")
        totalsent = 0
        print(f"{len(msg) = }")
        while totalsent < len(msg):
            print(f"{msg[totalsent:] = }")
            sent = self.sock.send(msg[totalsent:])
            print(f"{sent =}")
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
            print("Ending mysend")
    
    def myreceive(self):
        print("Starting myreceive")
        chunks = []
        bytes_recd = 0
        while bytes_recd < 1024:
            chunk = self.sock.recv(1024)
            if chunk == b'':
                print("socket connection broken")
                break
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            print(chunks)
        print("Ending myreceive")
        return b''.join(chunks)


connection = MySocket()
connection.connect("127.0.0.1", 65433)
connection.mysend(b"Hello, world")
print(connection.myreceive())
