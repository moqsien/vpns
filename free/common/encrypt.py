import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decode_base64(content:str)->bytes:
    length = len(content)
    count = 4-(length%4)
    if count > 0 and count < 4:
        content += "="*count
    bstr = base64.b64decode(content)
    return bstr

class AESCrypt(object):
    def __init__(self, password:bytes=b"x^)dixf&*1$free]"):
        self.password = password
    
    def Encrypt(self, content:str)->bytes:
        c = AES.new(self.password, AES.MODE_CBC, self.password[:AES.block_size])
        return c.encrypt(pad(content.encode(), AES.block_size))
    
    def Decrypt(self, content:str)->bytes:
        c = AES.new(self.password, AES.MODE_CBC, self.password[:AES.block_size])
        return unpad(c.decrypt(content), AES.block_size)

if __name__ == "__main__":
    p = os.path.join(os.path.abspath("."), "free\\common\\conf.txt")
    with open(p, "rb") as f:
        r = f.read()
        ac = AESCrypt()
        s = ac.Decrypt(r)
        print(s)
