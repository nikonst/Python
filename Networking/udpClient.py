import socket

def main():

    host = "127.0.0.01"
    port = 5001

    server = ("127.0.0.01", 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    s.bind((host, port))

    print("UPD Client Started")

    message = input("Message ->")
    while message != "q":
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server " + data.decode())
        message = input("Message ->")
    s.close()

if __name__ == "__main__":
    main()