import socket

def main():

    host = "127.0.01"
    port = 5000

    s = socket.socket()
    s.connect((host, port)) # Connect, not Bind !!!

    message = input("Message ->")
    while message != "q":
        s.send(message.encode())
        data = s.recv(1024)
        print("Received from server: " + data.decode())
        message = input("Message ->")

    s.close()

if __name__ == "__main__":
    main()

