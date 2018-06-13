import hashlib as hsh
import getpass
import json
from Device_Connectivity import NetworkConnection

class UserAccount:
    
    #Main function for account creation
    def account(self):        
        #Opening JSON file which holds usernames and hashed/salted passwords
        try:
            with open("data.json", "r") as inFile:
                self.database = json.load(inFile)
            inFile.close()
        except:
            pass

        #Code block invoking login or account creation
        while True:
            invoke = str(input("New user or login (nu/l/x/d): "))

            #If new user command invoked
            if invoke == "nu":
                #Storing new username
                user = str(input("Enter username: "))
                #Using getpass to obfuscate password input to interpreter
                uInput = str.encode(getpass.getpass("Enter password: "))

                #Salting and hashing password
                passOne = self.hashValues(uInput)               

                #Requesting user to re-enter same password again
                uInputTwo = str.encode(getpass.getpass("Enter password again: "))
                passTwo = self.hashValues(uInputTwo)

                #Checking if username is already taken
                if user in self.database:
                    print("Username already exists, please use different username")
                    pass
                #Checking if both passwords entered match
                elif passOne == passTwo:
                    print("Passwords match")
                    #Adding password to dictionary assigned to username as key
                    self.database[user] = passTwo
                    print(self.database)

                    #Opening and writing new username and hashed password to JSON out file
                    with open("data.json", "w") as outFile:
                        json.dump(self.database, outFile)
                    outFile.close()

                #Passwords dont match return to initial state   
                else:
                    print("Password dont match")
                    

            #If login command invoked
            elif invoke == "l":                

                #Requesting user input username and password and storing values to variables
                user = str(input("Enter username: "))
                uInput = str.encode(getpass.getpass("Enter password: "))        

                passW = self.hashValues(uInput)
                #Authenticate username is in database and hashed and salted password value is assigned to particular username
                if user in self.database and passW == self.database[user]:
                    print("Login successful, welcome %s" % (user))
                    #Getting host IP after successful user account authentication
                    self.ip = NetworkConnection.device_status()
                    print(self.ip)                    
                else:
                    print("incorrect username/password combination")

            #Command used for exiting program        
            elif invoke == "x":
                break

            #Command used for testing purposes - prints out current dictionary of usernames and hashed passwords
            elif invoke == "d":
                print(self.database)
    
    #Funtion for hashing and salting
    def hashValues(self, value):
        #Initialising new hash variable
        hashval = hsh.sha512()
        
        #Salting and hashing password
        hashval.update(b'salt')
        hashval.update(value)
        #Digesting hex hash values
        hashedPassword = hashval.hexdigest()

        return hashedPassword
    
    def main(self):
        self.database = {}       
        self.account()

if __name__ == "__main__":
    Account = UserAccount()
    Account.main()