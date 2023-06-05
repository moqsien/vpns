import io
import os
import sys
sys.path.append("..")

import requests
from lxml import etree
from vpns.common.proxy import get_proxy, set_proxy

class SiteV2Cross:
    def __init__(self):
        self.url  = "https://v2cross.com/archives/1884"
        
    def get_resp(self)->str:
        print(get_proxy())
        resp = requests.get(self.url, proxies=get_proxy())
        return resp.text
    
    def parse(self)->str:
        content = self.get_resp()
        html = etree.HTML(content)
        result = html.xpath("//pre//text()")
        return "".join(result)
    
    def url(self)->str:
        return self.url

if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    if get_proxy() == dict():
        set_proxy("http://localhost:2019")
    s = SiteV2Cross()
    print(s.parse())
