import socket, _thread

class Authentication_Server():

    def receive_connection(self):
        #Defining host IP as server IP address which is where connections will be received
        IP_ADDRESS = ""
        PORT = 5000

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((IP_ADDRESS, PORT))
        print("Awaiting client connection")

        while True:
            #Data buffer size limit
            data, addr = sock.recvfrom(64024)

    def main(self):
        while True:
            #Generating new thread for each connection
            _thread.start_new_thread(self.receive_connection())

if __name__ == "__main__":
    Anubis = Authentication_Server()
    Anubis.main()
