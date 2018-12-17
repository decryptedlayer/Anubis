from Crypto.Cipher import Salsa20

class Salsa:

    def __init__(self):
        #Constructing key of 16 bits
        self.key = b'0123456789012345'
        self.cipher = Salsa20.new(self.key)
        self.plaintext = b"hello"

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
        #print(plain)

if __name__ == "__main__":
    Sal20 = Salsa()
    Sal20.main()
