from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class KeyAccess:
    def __init__(self):
        self.key = get_random_bytes(32)

    def keyGeneration(self, keyFile):    
        file_out = open(keyFile, "wb")
        file_out.write(self.key)
        file_out.close()
        
    def readKey(self, keyFile):
        file_in = open(keyFile, "rb")
        self.key = file_in.read()

        return self.key

class Encryption:
    
    def __init__(self):
        accessKey = KeyAccess()
        keyFile = "key.bin"
        self.keyRead = accessKey.readKey(keyFile)
        
    def encrypt(self, p):
        cipher = AES.new(self.keyRead, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(p)
        
        return cipher.nonce, tag, ciphertext

    def readCiphertext(self, file):
        inFile = open(file, "rb")
        nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
        return nonce,
        
    def decrypt(self, file):
        inFile = open(file, "rb")
        nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
        cipher = AES.new(self.keyRead, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        return data

kAccess = KeyAccess()
encryptAlgo = Encryption()
keyFile = "key.bin"
def key_access_testing(keyFile):
    try:
        kAccess.keyGeneration(keyFile)
        print(kAccess.readKey(keyFile))
        return True
    except:
        return False

def symmetric_encryption_testing(keyFile):

    plaintext = b"hello"
    encrypting = encryptAlgo.encrypt(plaintext)
    readCipher = encryptAlgo.readCiphertext(keyFile)
    decrypting = encryptAlgo.decrypt(keyFile)
    print(decrypting)

    
print(symmetric_encryption_testing(keyFile))
    
