import hashlib as hsh
import getpass

database = {}

hashval = hsh.sha512()

while True:
    invoke = str(input("New user or login (nu/l): "))
    
    if invoke == "nu":
        user = str(input("Enter username: "))
        shv = str.encode(getpass.getpass("Enter password: "))

        hashval.update(b'salt')
        hashval.update(shv)
        n = hashval.hexdigest()

        hashvalTwo = hsh.sha512()

        shv = str.encode(getpass.getpass("Enter password again: "))
        hashvalTwo.update(b'salt')
        hashvalTwo.update(shv)

        x = hashvalTwo.hexdigest()
        
        if n == x:
            print("Passwords match")
            database[user] = x
            print(database)
            hashval = hsh.sha512()
        else:
            print("Password dont match")
            hashval = hsh.sha512()

    elif invoke == "l":
        hashval = hsh.sha512()
        user = str(input("Enter username: "))
        shv = str.encode(getpass.getpass("Enter password: "))        
        
        hashval.update(b'salt')
        hashval.update(shv)
        n = hashval.hexdigest()

        if user in database and n == database[user]:
            print("Hello %s" % (user))
        else:
            print("incorrect username/password")


    
