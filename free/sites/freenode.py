# coding=UTF-8
import sys
sys.path.append(".")

from urllib.parse import urljoin
from lxml import etree
from free.common.proxy import get_proxy, set_proxy, SiteBase
from free.common.verify import verify_content

class SiteFreeNode(SiteBase):
    def __init__(self):
        super(SiteFreeNode, self).__init__()
        self.host = "https://freefq.com/"
        
    def get_resp(self, url: str)->str:
        resp  = self.request(url, useproxy=True)
        html = etree.HTML(resp)
        if html is None:
            print(f"Download [{url}] failed.")
            return ""
        result = html.xpath('//table[@class="box"]//a[1]/@href')
        if len(result) > 0:
            url = result[0]
            if not url.startswith('https://'):
                url = urljoin(self.host, url)
            resp = self.request(url, useproxy=True)
            html = etree.HTML(resp)
            if html is None:
                print(f"Download [{url}] failed.")
                return ""
            result = html.xpath('//td[@id="text"]//a[1]/@href')
            if len(result) > 0:
                url = result[0]
                if not url.startswith('https://'):
                    url = urljoin(self.host, url)
                resp = self.request(url, useproxy=True)
                html = etree.HTML(resp)
                if html is None:
                    print(f"Download [{url}] failed.")
                    return ""
                result = html.xpath('//p//text()')
                return "".join(result)
        return ""
        
    def parse(self)->str:
        result = list()
        url_list = [
            "https://freefq.com/v2ray/",
			"https://freefq.com/free-ssr/",
			"https://freefq.com/free-ss/",
			"https://www.freefq.com/free-xray/",
			"https://freefq.com/freeuser/",
			"https://freefq.com/free-trojan/"
        ]
        for url in url_list:
            print(f"processing {url}")
            content = self.get_resp(url)
            lines = content.split('\n')
            for line in lines:
                if verify_content(line):
                    result.append(line)
        return "".join(result).encode("utf-8")
    
    def url(self)->str:
        return self.host
    
    def __str__(self) -> str:
        return self.host

if __name__ == "__main__":
    if get_proxy() == dict():
        set_proxy("http://localhost:2019")
    s = SiteFreeNode()
    print(s.parse())
