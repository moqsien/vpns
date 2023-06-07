import os
import json

STORE_DIR_ENV_NAME = "FREE_VPN_STORE_DIR"

class Config(object):
    def __init__(self, file_path:str=""):
        self.dir: str = file_path if file_path else os.getcwd()
        self.path = os.path.join(self.dir, "free_vpn_config.json")
        print(self.path)
        self.dict: dict = dict()
        self.load()
        if len(self.dict) > 0:
            self._key = self.dict.get("key", "x^)dixf&*1$free]")
            self._store_dir = self.dict.get("store_dir", os.getcwd())
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
        self._key = input("Set encryption key:\n").strip(" ")
        self._store_dir = input("Set restore directory:\n").strip(" ")
        if len(self.key) != 16:
            self._key = "x^)dixf&*1$free]"
        if not os.path.exists(self.store_dir):
            self._store_dir = os.getcwd()
        self.dict["key"] = self._key
        self.dict["store_dir"] = self._store_dir
        self.save()

    @property
    def key(self):
        return self._key.encode("utf-8")
    
    @property
    def store_dir(self):
        return self._store_dir

if __name__ == "__main__":
    # TODO: config file stored to current working directory.
    print(os.getcwd())
