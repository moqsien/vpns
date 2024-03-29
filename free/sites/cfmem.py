# coding=UTF-8
import os
import sys
sys.path.append(".")
    
from lxml import etree
from free.common.proxy import SiteBase
from free.common.encrypt import decode_base64

class SiteCfmem(SiteBase):
    def __init__(self):
        super(SiteCfmem, self).__init__()
        self.url = "https://www.cfmem.com/search/label/free"
        
    def get_resp(self)->str:
        resp = self.request(self.url)
        html = etree.HTML(resp)
        if html is None:
            print(f"Download [{self.url}] failed.")
            return ""
        result = html.xpath('//h2[@class="entry-title"]/a/@href')
        if len(result) > 0:
            url = result[0]
            resp = self.request(url)
            return resp
        return ""
            
    def parse(self)->str:
        print(f"processing {self.url}...")
        content = self.get_resp()
        html = etree.HTML(content)
        if html is None:
            print(f"Download [{self.url}] failed.")
            return ""
        result = html.xpath('//span[@role="presentation"]/text()')
        if len(result) > 0:
            try:
                return str(decode_base64(result[0]), 'utf-8')
            except Exception as e:
                print(f"Parse [{self.url}] failed.")
                print(e)
        return ""
    
    def url(self)->str:
        return self.url
    
    def __str__(self) -> str:
        return self.url
        
if __name__ == '__main__':
    s = SiteCfmem()
    r = s.parse()
    print(r.split("\n"))
