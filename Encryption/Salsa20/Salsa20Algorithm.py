import bcrypt, binascii
from Crypto.Cipher import Salsa20

"""
Example concept of using Salsa20 as a private key messaging protocol
where both parties use a known hashed password in order to
to encrypt and decrypt messages.

Message authenticity is is not guaranteed unless use of HMAC Message
Authentication Code to authenticate ciphertext (encrypt-then-authenticate)
"""

class Salsa:

    def __init__(self):
        #Constructing secret key of 16 bits from hashed password
        self.key = self.password()

        #Checking function properties
        print(self.check(self.key))

        #Generating new Salsa20 Cipher
        self.cipher = Salsa20.new(self.key)
        
        #Defining example plaintext
        self.plaintext = str(input("Enter messaage: ")).encode()

    def hash(self, p):
        #Defining example salt value
        salt = b"1234"
        
        hv = bcrypt.kdf(p, salt, 64, 100)
        cipher = binascii.hexlify(hv)

        return cipher

    #Function for checking variable input properties
    def check(self, x):
        l, typ = len(x), type(x)

        return l, typ        

    #Function for generating hashed password used for encryption key
    def password(self):
        password = str(input("Enter Password of 16 characters: ")).encode()
        hashValue = self.hash(password)

        return hashValue[:16]

    #Salsa20 Encryption function
    def encrypt(self, c, p, k):
        #Generating new cipher based on key
        cipher = Salsa20.new(k)
        #Encrypting cipher
        ciphertext = c.encrypt(p)

        #Returning ciphertext and nonce used for decryption
        return ciphertext, c.nonce

    #Salsa20 Decryption function
    def decrypt(self, c, n, k):
        #Generating new cipher based on key and nonce
        cipher = Salsa20.new(k, n)

        #Decrypting cipher
        plaintext = cipher.decrypt(c)

        return plaintext.decode('utf-8')

    def main(self):
        #Defining local variables based on constructors
        cipher = self.cipher
        plaintext = self.plaintext
        key = self.key

        #Initialising functions for encryption and decryption
        encryption = self.encrypt(cipher, plaintext, key)
        decryption = self.decrypt(encryption[0], encryption[1], key)

        print(encryption[:])
        print(decryption)

if __name__ == "__main__":
    Sal20 = Salsa()
    Sal20.main()
