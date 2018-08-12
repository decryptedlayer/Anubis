import json, time, datetime
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_GCM_ALGORITHM:

    def __init__(self):
        self.header = b"Test"
        self.data = b"Hello"
        self.timestamp = (datetime.datetime.fromtimestamp(time.time())
                            .strftime("%Y-%m-%d %H:%M:%S"))        
        
    def GCM_Encryption(self):        
        try:
            self.key = get_random_bytes(32)
            cipher = AES.new(self.key, AES.MODE_GCM)
            cipher.update(self.header)
            ciphertext, tag = cipher.encrypt_and_digest(self.data)
            json_output = self.JSON_Output(cipher, self.header, ciphertext, tag)

        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)

        finally:
            return json_output
        

    def GCM_Decryption(self):
        try:
            b64 = self.JSON_Open_Database()
            json_k = ["nonce", "header", "ciphertext", "tag"]
            jv = {k:b64decode(b64[k]) for k in (json_k)}            
            cipher = AES.new(self.key, AES.MODE_GCM, nonce = jv["nonce"])
            cipher.update(jv["header"])
            plaintext = cipher.decrypt_and_verify(jv["ciphertext"], jv["tag"])

        
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)

        finally:
            return plaintext


    def JSON_Open_Database(self):
        try:
            with open("data.json", "r") as inFile:
                database = json.load(inFile)
            inFile.close()

        except:
            pass
        
        finally:
            return database

    def JSON_Save_Database(self, json_k, json_v):        
        result_dump = json.dumps(dict(zip(json_k, json_v)))
        with open("data.json", "w") as outFile:
            json.dump(dict(zip(json_k, json_v)), outFile)
        outFile.close()

        return result_dump

    def JSON_Output(self, cipher, header, ciphertext, tag):        
        json_k = ["nonce", "header", "ciphertext", "tag"]
        json_v = [b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag)]
        key_dump = self.JSON_Save_Database(json_k, json_v)
        
        return key_dump

    def main(self):
        print(self.GCM_Encryption())
        print(self.GCM_Decryption())
        #print(self.JSON_Open_Database())


if __name__ == "__main__":
    AESGCM =AES_GCM_ALGORITHM()
    AESGCM.main()
