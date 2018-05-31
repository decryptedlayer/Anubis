from sys import platform

class DeviceArchitecture:

    def system_architecture(self):
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

    def main(self):       
        print(self.system_architecture())

if __name__ == "__main__":
    Architecture = DeviceArchitecture()
    Architecture.main()
