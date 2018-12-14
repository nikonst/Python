import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serverSocket.bind((host,port))
serverSocket.listen()

while True:
    # establish a connection
    clientsocket, addr = serverSocket.accept()

    print("Got a connection from %s" % str(addr))

    msg = "Thank you for connecting" + "\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()

