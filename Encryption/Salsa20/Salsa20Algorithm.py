import bcrypt, binascii
from Crypto.Cipher import Salsa20

"""
Example concept of using Salsa20 as a private key messaging protocol
where both parties use a known hashed password in order to
to encrypt and decrypt messages.
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
        self.plaintext = b"hello"

    def hash(self, p):
        #Defining example salt value
        salt = b"1234"
        
        hv = bcrypt.kdf(p, salt, 64, 100)
        cipher = binascii.hexlify(hv)

        return cipher

    def check(self, x):
        l, typ = len(x), type(x)

        return l, typ
        

    def password(self):
        password = str(input("Enter Password of 16 characters: ")).encode()
        hashValue = self.hash(password)

        return hashValue[:16]
    
    def encrypt(self, c, p):
        ciphertext = c.encrypt(p)

        #Returning ciphertext and nonce to be sent to receiver
        return ciphertext, c.nonce

    def decrypt(self, c, n, k):
        x = 2
        #cipher = Salsa20.new(k, n)
        #plaintext = cipher.decrypt(c)

        return x

    def main(self):
        cipher = self.cipher
        plaintext = self.plaintext
        ciphertext = self.encrypt(cipher, plaintext)
        plain = self.decrypt(cipher, ciphertext[1], self.key)

        print(ciphertext[:])

if __name__ == "__main__":
    Sal20 = Salsa()
    Sal20.main()
