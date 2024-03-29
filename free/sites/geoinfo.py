# coding=UTF-8
import os
import sys
sys.path.append(".")

import requests
from free.common.conf import STORE_DIR_ENV_NAME

geoinfo_download_urls = {
    "geoip.db":    "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2Flyc8503%2Fsing-box-rules%2Freleases%2Flatest%2Fdownload%2Fgeoip.db",
    "geosite.db":  "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2Flyc8503%2Fsing-box-rules%2Freleases%2Flatest%2Fdownload%2Fgeosite.db",
    "geoip.dat":   "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2FLoyalsoldier%2Fv2ray-rules-dat%2Freleases%2Flatest%2Fdownload%2Fgeoip.dat",
    "geosite.dat": "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2FLoyalsoldier%2Fv2ray-rules-dat%2Freleases%2Flatest%2Fdownload%2Fgeosite.dat",
}
    
class DownloadGeoInfo(object):
    def __init__(self):
        self.urls = geoinfo_download_urls
    
    def parse(self)->str:
        store_dir = os.environ.get(STORE_DIR_ENV_NAME)
        if not store_dir:
            store_dir = os.getcwd()

        for name, url in self.urls.items():
            print(f"Downloading {name}...")
            resp = requests.get(url)
            with open(os.path.join(store_dir, name), 'wb') as f:
                f.write(resp.content)
        return ""

if __name__ == '__main__':
    d = DownloadGeoInfo()
    d.parse()
