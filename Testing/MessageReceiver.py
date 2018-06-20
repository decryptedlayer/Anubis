import socket

class MessageReceiver:
    
    def receive(self):
        IP = ''
        PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((IP, PORT))
        print("Awaiting to receive connection...")

        while True:
            #Buffer size of data
            data, self.addr = self.sock.recvfrom(64024)
            print(daa.decode())
            print("Awaiting to receive connection...")

    def main(self):
        self.receive()

if __name__ == "__main__":
    r = MessageReceiver()
    r.main()
