from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def keyGeneration():    
    key = get_random_bytes(32)
    file_out = open("key.bin", "wb")
    file_out.write(key)
    file_out.close()
    
def readKey():
    file_in = open("key.bin", "rb")
    key = file_in.read()

    return key

def encrypt(p):
    k = readKey()
    cipher = AES.new(k, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(p)
    
    return cipher.nonce, tag, ciphertext

def readCiphertext(file):
    nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
    return nonce,
    
def decrypt(key, file):
    inFile = open(file, "rb")
    nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data
    
def encryptionTesting(plaintext):
    
    try:
        readCiphertext(file)
        encrypt(plaintext, 01462673152
                key, file)
        decrypt(key, file)
    except:
        pass
    
    return readCiphertext(file)

