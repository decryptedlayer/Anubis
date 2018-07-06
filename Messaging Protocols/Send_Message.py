import socket
from Encryption_Algorithm import *

class MessageSender:
    def send(self, p):
        IP = '10.123.155.131' # IP associated with host the Receiver
        PORT = 5000
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(p.encode(), (IP, PORT))

    def main(self):
        message = encrypt("Test")        
        self.send(message)

if __name__ == "__main__":
    sm = MessageSender()
    sm.main()
