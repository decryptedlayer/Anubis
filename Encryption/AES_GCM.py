from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_GCM:
    def __init__(self):        
        self.data = b"hello"
        
        #32 random byted for 256-bit encryption key
        self.key = get_random_bytes(32)

    def writeKey(self, key):
        file_out = open("key.bin", "wb")
        file_out.write(key) 
        file_out.close()


    def importKey(self):
        sessionKey = b""
        file_in = open("key.bin", "rb")
        for i in file_in:
            sessionKey = i
        return(sessionKey)

    def encryption(self):
        #Generating new cipher and initialising block cipher mode of operation
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(self.data)

        file_out = open("encrypted.bin", "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        file_out.close()

        #Writing out current session key
        self.writeKey(self.key)

        return self.key

    def decryption(self):        
        file_in = open("encrypted.bin", "rb")
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
        file_in.close()

        cipher = AES.new(self.key, AES.MODE_GCM, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        return data.decode("utf-8")

    def keyIntegrityCheck(self):
        if self.importKey() == self.key:
            return True
        else:
            return False

    def main(self):
        print(self.encryption())
        print(self.decryption())
        print(self.importKey())
        print(self.keyIntegrityCheck())

if __name__ == "__main__":
    AESEncryption = AES_GCM()
    AESEncryption.main()

