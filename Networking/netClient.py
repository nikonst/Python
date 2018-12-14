import socket

# create a socket object
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
socketClient.connect((host, port))

# Receive no more than 1024 bytes
msg = socketClient.recv(1024)

socketClient.close()
print (msg.decode('ascii'))