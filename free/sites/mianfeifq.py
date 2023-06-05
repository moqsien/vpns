# coding=UTF-8
import sys
sys.path.append(".")

import json
from lxml import etree
from free.common.proxy import SiteBase

class SiteMianfeifq(SiteBase):
    def __init__(self):
        super(SiteMianfeifq, self).__init__()
        self.url = "https://gitlab.com/mianfeifq/share/-/blob/master/README.md?format=json&viewer=rich"
        
    def get_resp(self)->str:
        resp = self.request(self.url)
        json_resp = json.loads(resp)
        html_str = json_resp["html"]
        return html_str
    
    def parse(self)->str:
        print(f"processing {self.url}...")
        html_str = self.get_resp()
        html = etree.HTML(html_str)
        if html is None:
            print(f"Download [{self.url}] failed.")
            return ""
        result = html.xpath("//code/span/text()")
        return "\n".join(result)
    
    def url(self)->str:
        return self.url
    
    def __str__(self) -> str:
        return self.url
    
if __name__ == "__main__":
    s = SiteMianfeifq()
    print(s.parse())
