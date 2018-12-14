import socket

def main():

    host = "127.0.0.01"
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    s.bind((host, port))

    print("UPD Server Started")

    while True:
        data, addr = s.recvfrom(1024)
        print("Message from : " + str(addr))
        print("From connected user: " + str(data))
        data = str(data).upper()
        print("Sending : " + data)
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == "__main__":
    main()
