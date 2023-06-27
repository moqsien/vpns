# coding=UTF-8
# import os
import json
import sys
sys.path.append(".")
    
from lxml import etree
from free.common.proxy import SiteBase
from free.common.encrypt import decode_base64

class SiteCfmemRSS(SiteBase):
    def __init__(self):
        super(SiteCfmemRSS, self).__init__()
        self.url = "https://www.cfmem.com/feeds/posts/default?alt=json"
        
    def get_resp(self)->str:
        result = []
        resp = self.request(self.url)
        json_dict = json.loads(resp)
        entries = json_dict.get("feed", {}).get('entry')
        for entry in entries:
            content = entry.get('content', {}).get('$t')
            html = etree.HTML(content)
            span_list = html.xpath("//pre/span/text()")
            for span in span_list:
                r = decode_base64(span)
                r = r.decode("utf-8")
                if len(r) > 0:
                    result.append(r)
        return "\n".join(result)
            
    def parse(self)->str:
        print(f"processing {self.url}...")
        return self.get_resp()
        
    def url(self)->str:
        return self.url
    
    def __str__(self) -> str:
        return self.url
        
if __name__ == '__main__':
    s = SiteCfmemRSS()
    r = s.parse()
    print(r.split("\n"))
