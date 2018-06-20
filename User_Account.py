import getpass, json, random, string, binascii, bcrypt, sys
from Local_Device import InterrogateDevice

class UserAccount:
    
    #Function for opening and returning database contents
    def open_database():
        #Opening JSON file which holds usernames, hashed passwords and associated salts
        try:
            with open("data.json", "r") as inFile:
                database = json.load(inFile)
            inFile.close()
            return database
        except:
            pass

    #Function for creating new user account
    def create_account():        
        database = UserAccount.open_database()
        #Storing new username
        user = str(input("Enter username: "))
        #Using getpass to obfuscate password input to interpreter
        uInput = str.encode(getpass.getpass("Enter password: "))
        #Generating new random salt value
        slt = UserAccount.saltValue()                
        #Salting and hashing password
        passOne = UserAccount.hashValues(uInput, slt)
        #Requesting user to re-enter same password again
        uInputTwo = str.encode(getpass.getpass("Enter password again: "))
        #Hashing and salting second password input
        passTwo = UserAccount.hashValues(uInputTwo, slt)
                
        #Checking if username is already taken
        if user in database:
            print("Username already exists, please use different username")
            pass                
        #Checking if both passwords entered match
        elif passOne == passTwo:
            print("Passwords match")
            #Adding hashed password and salt to dictionary assigned to username as key
            database[user]= [passTwo, slt.decode('ascii'), InterrogateDevice.device_status(), InterrogateDevice.system_architecture()]
            #Opening and writing new username and hashed password to JSON out file
            with open("data.json", "w") as outFile:
                json.dump(database, outFile)
            outFile.close()
        #Passwords dont match return to initial state   
        else:
            print("Passwords dont match")

    #Function for logging into account
    def login_account():
        database = UserAccount.open_database()
        #Requesting user input username and password and storing values to variables
        user = str(input("Enter username: "))
        uInput = str.encode(getpass.getpass("Enter password: "))                
        #Authenticate username is in database and hashed and salted password value is assigned to particular username
        if user in database:
            #Extracting original salt associated with username
            uSlt = database[user][1]
            #Encoding associated salt into binary
            uSlt = str.encode(uSlt)
            #Hashing and salting password for user to login
            passW = UserAccount.hashValues(uInput, uSlt)
            #Verifying hashed and salted password input same as hashed salted password in database
            if passW == database[user][0]:
                print("-----------------\nLogin successful!")                        
                #Getting host IP after successful user account authentication
                ip = InterrogateDevice.device_status()
                device = InterrogateDevice.system_architecture()
                print("IP: %s\nOS: %s" % (ip, device))
                #Updating database with new device IP address which user logged in with
                database[user][2] = ip
                #Writing change of IP address to database
                with open("data.json", "w") as outFile:
                    json.dump(database, outFile)
                outFile.close()                        
                UserAccount.userAccount(user)
            else:
                print("Incorrect username or password combination")

    #Function for printing database contents
    def print_database():
        #Command used for testing purposes - prints out current dictionary of usernames and hashed passwords
        database = UserAccount.open_database()
        print(database)
    
    #Funtion for hashing and salting
    def hashValues(value, salt):        
        #Encoding salt from string to binary
        hashVal = bcrypt.kdf(value, salt, 64, 100)
        #Generating hex value from binary hash
        key = binascii.hexlify(hashVal)        
        #Returning decoded hex value
        return key.decode('ascii')

    #Function for generating semi-random salt values
    def saltValue():
        #Utilising bcrypt to generate random salt values
        slt = bcrypt.gensalt(20)
        return slt

    def userAccount(user):
        invoke = str(input("\nHi %s do you want to log-off your account or exit program (lf/x): " % (user[0].upper()+user[1:])))
        if invoke.lower() == "lf":
            print("Logging off...")
            UserAccount.create_account()
        elif invoke.lower() == "x":
            print("Exiting program...")
            sys.exit()
        else:
            print("Unknown command")
