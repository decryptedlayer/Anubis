from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_EAX:

    def encrypt(self, p, key):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(p)
        file_out = open("encrypted.bin", "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

    def decrypt(self, key):
        inFile = open("encrypted.bin", "rb")
        nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        return data
    
    def main(self):
        key = get_random_bytes(32)
        plaintext = b"test"
        self.encrypt(plaintext, key)
        print(self.decrypt(key))
        

if __name__ == "__main__":
    AESEAX = AES_EAX()
    AESEAX.main()
