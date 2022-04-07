import socket


HOST, PORT = "127.0.0.1", 65433
# create a basic socket server
# create a loop to always listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)
        data_length = len(data)
        print(f"{data = }, {data_length = }")
        sent_data = 0
        while sent_data < data_length:
            if not data:
                break
            conn.sendall(data)
            print("sent")
            sent_data += len(data)

