# coding=UTF-8
from free.sites.cfmem import SiteCfmem
from free.sites.freenode import SiteFreeNode
from free.sites.frees import SiteFreeSubscribes
from free.sites.geoinfo import DownloadGeoInfo
from free.sites.mianfeifq import SiteMianfeifq
from free.sites.v2cross import SiteV2Cross
from free.sites.wenpblog import SiteWenpBlog

class VPN(object):
    def __init__(self):
        self.tasks = [
            SiteCfmem(),
            SiteFreeNode(),
            SiteFreeSubscribes(),
            DownloadGeoInfo(),
            SiteMianfeifq(),
            SiteV2Cross(),
            SiteWenpBlog(),
        ]
        self.vmess = []
        self.vless = []
        self.trojan = []
        self.ss = []
        self.ssr = []
        
    def parse(self, contet:str):
        pass
    
    def run(self):
        for task in self.tasks:
            content = task.parse()
            if content == "":
                continue
            else:
                self.parse(content)
            