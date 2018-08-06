from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_EAX:
    def __init__(self):        
        self.data = b"hello"
        self.key = get_random_bytes(16)

    def writeKey(self, key):
        file_out = open("key.bin", "wb")
        file_out.write(key) 
        file_out.close()


    def importKey(self):
        sessionKey = str()
        file_in = open("key.bin", "rb")
        for i in file_in:
            sessionKey = i
        return(sessionKey)

    def encryption(self):       
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.data)

        file_out = open("encrypted.bin", "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        file_out.close()

        self.writeKey(self.key)

        return self.key

    def decryption(self):        
        file_in = open("encrypted.bin", "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
        file_in.close()

        cipher = AES.new(self.key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        return data

    def main(self):
        print(self.encryption())
        print(self.decryption())
        #print(self.importKey())

if __name__ == "__main__":
    AESEncryption = AES_EAX()
    AESEncryption.main()

