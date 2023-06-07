# coding=UTF-8
import os
import json
import datetime
import subprocess
from free.sites.cfmem import SiteCfmem
from free.sites.freenode import SiteFreeNode
from free.sites.frees import SiteFreeSubscribes
from free.sites.geoinfo import DownloadGeoInfo
from free.sites.mianfeifq import SiteMianfeifq
from free.sites.v2cross import SiteV2Cross
from free.sites.wenpblog import SiteWenpBlog
from free.common.proxy import set_proxy, get_proxy
from free.common.encrypt import AESCrypt
from free.common.conf import Config

class VPN(object):
    def __init__(self):
        self.cwd = os.getcwd()
        self.tasks = [
            SiteCfmem(),
            SiteFreeSubscribes(),
            SiteFreeNode(),
            SiteMianfeifq(),
            SiteWenpBlog(),
            SiteV2Cross(),
            DownloadGeoInfo(),
        ]
        self.vmess = []
        self.vless = []
        self.trojan = []
        self.ss = []
        self.ssr = []
        self.other = []
        self.filename = "conf.txt"
        self.conf = Config()
        self.store_dir = self.conf.store_dir
        self.key = self.conf.key
    
    def parse_other(self, line:str):
        if line.find("vmess://"):
            scheme = "vmess://"
            result = self.vmess
        elif line.find("vless://"):
            scheme = "vless://"
            result = self.vless
        elif line.find("ss://"):
            scheme = "ss://"
            result = self.ss
        elif line.find("ssr://"):
            scheme = "ssr://"
            result = self.ssr
        elif line.find("trojan://"):
            scheme = "trojan://"
            result = self.trojan
        else:
            print(f"Unsupported vpn scheme: {line}")
            if line not in self.other:
                self.other.append(line)  
            return
        ll = line.split(scheme)
        if len(ll) == 2:
            result.append(f"{scheme}{ll[1]}")
        
    def parse(self, content:str):
        for line in content.split("\n"):
            if line.find("[") > 0:
                continue
            line = line.strip("\r")
            if line.startswith("vmess://"):
                if line not in self.vmess:
                    self.vmess.append(line)
            elif line.startswith("vless://"):
                if line not in self.vless:
                    self.vless.append(line)
            elif line.startswith("ss://"):
                if line not in self.ss:
                    self.ss.append(line)
            elif line.startswith("ssr://"):
                if line not in self.ssr:
                    self.ssr.append(line)
            elif line.startswith("trojan://"):
                if line not in self.trojan:
                    self.trojan.append(line)
            else:
                self.parse_other(line)
    
    def run(self):
        for task in self.tasks:
            try:
                content = str(task.parse())
            except Exception as e:
                content = ""
                print(e)
            if content == "":
                continue
            else:
                self.parse(content)
        if any([self.vmess, self.vless, self.ss, self.ssr, self.trojan]):
            self.save_file("vpn.json")
            self.git_push()
    
    def save_file(self, filename:str):
        result = {
            "vmess": {"list": self.vmess, "total": len(self.vmess)},
            "vless": {"list": self.vless, "total": len(self.vless)},
            "ss": {"list": self.ss, "total": len(self.ss)},
            "ssr": {"list": self.ssr, "total": len(self.ssr)},
            "trojan": {"list": self.trojan, "total": len(self.trojan)},
            "other": {"list": self.other, "total": len(self.other)},
            "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)
            
        json_str = json.dumps(result, indent=4, ensure_ascii=True)
        crypto = AESCrypt()
        content = crypto.Encrypt(json_str)
        with open(os.path.join(self.store_dir, self.filename), "wb") as f:
            f.write(content)
            
    def git_push(self):
        git_dir = os.path.join(self.store_dir, ".git")
        if  os.path.exists(git_dir):
            os.chdir(self.store_dir)
            subprocess.call(["git", "add", "."])
            subprocess.call(["git", "commit", "-m", "update"])
            subprocess.call(["git", "push"])
            os.chdir(self.cwd)
            

if __name__ == "__main__":
    # TODO: add config file and auto git push.
    if not get_proxy():
        set_proxy("http://localhost:2019")
    v = VPN()
    v.run()
