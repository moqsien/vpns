# coding=UTF-8
import os
import sys
sys.path.append(".")

import requests
from free.common.conf import STORE_DIR_ENV_NAME
    
class DownloadCloudFlare(object):
    def __init__(self):
        self._ipv4_url = "https://www.cloudflare.com/ips-v4"
        self._ipv6_url = "https://www.cloudflare.com/ips-v6"
    
    def parse(self)->str:
        store_dir = os.environ.get(STORE_DIR_ENV_NAME)
        if not store_dir:
            store_dir = os.getcwd()

        print(f"Downloading {self._ipv4_url}...")
        resp = requests.get(self._ipv4_url)
        with open(os.path.join(store_dir, "cloudflare_ipv4.txt"), 'wb') as f:
            f.write(resp.content)
            
        print(f"Downloading {self._ipv6_url}...")
        resp = requests.get(self._ipv6_url)
        with open(os.path.join(store_dir, "cloudflare_ipv6.txt"), 'wb') as f:
            f.write(resp.content)
        return ""

if __name__ == '__main__':
    d = DownloadCloudFlare()
    d.parse()
