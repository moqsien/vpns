# coding=UTF-8
import requests
    
class DownloadGeoInfo(object):
    def __init__(self):
        self.urls = {
            "geoip.db":    "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2Flyc8503%2Fsing-box-rules%2Freleases%2Flatest%2Fdownload%2Fgeoip.db",
            "geosite.db":  "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2Flyc8503%2Fsing-box-rules%2Freleases%2Flatest%2Fdownload%2Fgeosite.db",
            "geoip.dat":   "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2FLoyalsoldier%2Fv2ray-rules-dat%2Freleases%2Flatest%2Fdownload%2Fgeoip.dat",
            "geosite.dat": "https://ghproxy.com/?q=https%3A%2F%2Fgithub.com%2FLoyalsoldier%2Fv2ray-rules-dat%2Freleases%2Flatest%2Fdownload%2Fgeosite.dat",
        }
    
    def parse(self)->str:
        for name, url in self.urls.items():
            print(f"Downloading {name}...")
            resp = requests.get(url)
            with open(name, 'wb') as f:
                f.write(resp.content)
        return ""

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    d = DownloadGeoInfo()
    d.parse()
