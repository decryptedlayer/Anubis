import requests, socket

class NetworkConnection:
    
    #Function for verifying device connection status and returning local IP
    def device_status():
        try:
            #Verifying IPV4 connectivity and DNS resolution
            requests.get("http://www.msftncsi.com", timeout=3)
            #Returning device IP address if connnection found
            return NetworkConnection.device_ip()
        except requests.ConnectionError:
            pass
        return False

    #Function for getting device IP address
    def device_ip():
        try:
            #Opening socket
            netSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #Connecting to IP 8.8.8.8 on port 80
            netSocket.connect(("8.8.8.8.", 80))
            #Getting local IP through socketname
            ip_address = netSocket.getsockname()[0]
            netSocket.close()
            return ip_address
        except Exception:
            return False
    
