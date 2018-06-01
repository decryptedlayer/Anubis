import hashlib as hsh
import getpass

class UserAccount:

    def account(self):
        
        while True:
            invoke = str(input("New user or login (nu/l/x/d): "))

            self.hashval = hsh.sha512()
            self.hashvalTwo = hsh.sha512()
            
            if invoke == "nu":
                user = str(input("Enter username: "))
                shv = str.encode(getpass.getpass("Enter password: "))

                self.hashval.update(b'salt')
                self.hashval.update(shv)
                hashedPassword = self.hashval.hexdigest()                

                shv = str.encode(getpass.getpass("Enter password again: "))
                self.hashvalTwo.update(b'salt')
                self.hashvalTwo.update(shv)

                x = self.hashvalTwo.hexdigest()

                if user in self.database:
                    print("Username already exists, please use different username")
                    pass
                elif hashedPassword == x:
                    print("Passwords match")
                    self.database[user] = x
                    print(self.database)
                    self.hashval = hsh.sha512()
                else:
                    print("Password dont match")
                    self.hashval = hsh.sha512()

            elif invoke == "l":
                self.hashval = hsh.sha512()
                user = str(input("Enter username: "))
                shv = str.encode(getpass.getpass("Enter password: "))        
            
                self.hashval.update(b'salt')
                self.hashval.update(shv)
                hashedPassword = self.hashval.hexdigest()

                if user in self.database and hashedPassword == self.database[user]:
                    print("Login successful, welcome %s" % (user))
                else:
                    print("incorrect username/password combination")
                    
            elif invoke == "x":
                break

            elif invoke == "d":
                print(self.database)

    def main(self):
        self.database = {}
        
        
        self.account()

if __name__ == "__main__":
    Account = UserAccount()
    Account.main()
    
