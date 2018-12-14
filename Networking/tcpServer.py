import socket

def main():

    host = "127.0.0.01"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1) # Number of connection at a time

    conn, addr = s.accept()

    print("Connection from:"+str(addr))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("\nMe as a server I received "+str(data)+"from client:"+str(addr))
        # I capitalize the string
        data = str(data).upper()
        print("I will now send the capitalized string...")
        #send data to the connection
        conn.send(data.encode())
    #Close the socket
    conn.close()

if __name__ == "__main__":
    main()

