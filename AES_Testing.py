from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(p, key, file):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(p)
    file_out = open(file, "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

def readCiphertext(file):
    inFile = open(file, "rb")
    nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
    return nonce,
    
def decrypt(key, file):
    inFile = open(file, "rb")
    nonce, tag, ciphertext = [inFile.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data
    
def encryptionTesting(plaintext):
    key = get_random_bytes(32)
    #plaintext = b"test"
    file = "misc.bin"
    try:
        readCiphertext(file)
        encrypt(plaintext, key, file)
        decrypt(key, file)
    except:
        pass
    
    return readCiphertext(file)

