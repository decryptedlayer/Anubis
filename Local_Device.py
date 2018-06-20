import requests, socket
from sys import platform

class InterrogateDevice:
    
    #Function for verifying device connection status and returning local IP
    def device_status():
        try:
            #Verifying IPV4 connectivity and DNS resolution
            requests.get("http://www.msftncsi.com", timeout=3)
            #Returning device IP address if connnection found
            return InterrogateDevice.device_ip()
        except requests.ConnectionError:
            pass
        return False

    #Function for getting device IP address
    def device_ip():
        try:
            #Opening socket
            netSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #Connecting to Google Public DNS recursive name servers on port 80
            netSocket.connect(("8.8.8.8.", 80))
            #Getting local IP through socketname
            ip_address = netSocket.getsockname()[0]
            #Closing socket
            netSocket.close()
            return ip_address
        except Exception:
            return False

    #Getting architecture of local device user running
    def system_architecture():
        try:
            if platform == "linux" or platform == "linux2":
                return "Linux"
            elif platform == "darwin":
                return "OS X"
            elif platform == "win32":
                return "Windows"
            else:
                raise Exception
        except Exception:
            pass
        return False
    
