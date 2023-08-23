import os
import json
import random
import string
import pathlib

STORE_DIR_ENV_NAME = "FREE_VPN_STORE_DIR"

DEFAULT_AES_KEY = "x^)dixf&*1$free]"
DEFAULT_LOCAL_PROXY = "http://localhost:2019"

def get_home_dir():
    homedir = str(pathlib.Path.home())
    return homedir

class Config(object):
    def __init__(self, file_path:str=""):
        homedir = get_home_dir()
        self.dir: str = file_path if file_path else homedir
        self.path = os.path.join(self.dir, "free_vpn_config.json")
        self.dict: dict = dict()
        self.load()
        if len(self.dict) > 0:
            self._key = self.dict.get("key", DEFAULT_AES_KEY)
            self._store_dir = self.dict.get("store_dir", homedir)
            self._proxy = self.dict.get("proxy", DEFAULT_LOCAL_PROXY)
        else:
            self.set_config()
        store_dir = getattr(self, "store_dir")
        if store_dir:
            os.environ.setdefault(STORE_DIR_ENV_NAME, store_dir)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.dict = json.load(f)

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.dict, f, indent=4, ensure_ascii=True)

    def set_config(self):
        print("How to set AES encryption key:")
        print("1> Set encryption key by default.[Default]")
        print("2> Set encryption key by input.")
        print("3> Set encryption key by auto-generation.") 
        operation = input("Choose 1, 2 or 3, then press <Enter>: ").strip(" ")
        if not operation:
            operation = "1"
            
        print(f"You have chosen [{operation}]")
        if operation == "1":
            self._key = DEFAULT_AES_KEY
        elif operation == "2":
            self._key = input("Please input your encryption key [length should be 16]: ")
        else:
            self._key = self.random_key()
        
        self._store_dir = input("Set restore directory:\n").strip(" ")
        self._proxy = input("Set local proxy:\n").strip(" ")
        
        if len(self.key) != 16:
            self._key = DEFAULT_AES_KEY
        if not os.path.exists(self.store_dir):
            self._store_dir = get_home_dir()
        if not self._proxy:
            self._proxy = DEFAULT_LOCAL_PROXY
        self.dict["key"] = self._key
        self.dict["store_dir"] = self._store_dir
        self.dict["proxy"] = self._proxy
        print("You are saving freevpn config file...")
        print(f"EncryptionKey: [ {self._key} ], StoreDir: [ {self._store_dir} ], LocalProxy: [ {self._proxy} ]")
        self.save()

    @property
    def key(self)->bytes:
        return self._key.encode("utf-8")
    
    @property
    def store_dir(self)->str:
        return self._store_dir
    
    @property
    def proxy(self):
        return self._proxy
    
    def random_key(self)->str:
        sample_str_all = string.ascii_letters + string.digits + "!@#$*"
        _key = "n" + "".join(random.sample(sample_str_all, 15))
        return _key

if __name__ == "__main__":
    print(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890',16))
    print(string.punctuation)
