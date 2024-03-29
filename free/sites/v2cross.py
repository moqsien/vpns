# coding=UTF-8
import sys
sys.path.append(".")

from lxml import etree
from free.common.proxy import get_proxy, set_proxy, SiteBase

class SiteV2Cross(SiteBase):
    def __init__(self):
        super(SiteV2Cross, self).__init__()
        self.url  = "https://v2cross.com/archives/1884"
        
    def get_resp(self)->str:
        resp =  self.request(self.url, useproxy=True)
        return resp
    
    def parse(self)->str:
        print(f"processing {self.url}...")
        content = self.get_resp()
        html = etree.HTML(content)
        if html is None:
            print(f"Download [{self.url}] failed.")
            return ""
        result = html.xpath("//pre//text()")
        return "".join(result)
    
    def url(self)->str:
        return self.url
    
    def __str__(self) -> str:
        return self.url

if __name__ == "__main__":
    if get_proxy() == dict():
        set_proxy("http://localhost:2019")
    s = SiteV2Cross()
    r = s.parse()
    sList = r.split("\n")
    for i in sList:
        try:
            print(i)
        except Exception as e:
            print(e)
