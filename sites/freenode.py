import io
import sys
sys.path.append("..")

from urllib.parse import urljoin
import requests
from lxml import etree
from vpns.common.proxy import get_proxy, set_proxy
from vpns.common.verify import verify_content

# https://www.freefq.com
class SiteFreeNode:
    def __init__(self):
        self.host = "https://freefq.com/"
        
    def get_resp(self, url: str)->str:
        resp  = requests.get(url, proxies=get_proxy(), timeout=120)
        html = etree.HTML(resp.text)
        result = html.xpath('//table[@class="box"]//a[1]/@href')
        if len(result) > 0:
            url = result[0]
            if not url.startswith('https://'):
                url = urljoin(self.host, url)
            print(url)
            resp = requests.get(url, proxies=get_proxy(), timeout=120)
            html = etree.HTML(resp.text)
            result = html.xpath('//td[@id="text"]//a[1]/@href')
            if len(result) > 0:
                url = result[0]
                if not url.startswith('https://'):
                    url = urljoin(self.host, url)
                print(url)
                resp = requests.get(url, proxies=get_proxy(), timeout=120)
                html = etree.HTML(resp.text)
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
            print(url)
            content = self.get_resp(url)
            lines = content.split('\n')
            for line in lines:
                if verify_content(line):
                    result.append(line)
        return "".join(result)
    
    def url(self)->str:
        return self.host

if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    if get_proxy() == dict():
        set_proxy("http://localhost:2019")
    s = SiteFreeNode()
    print(s.parse())
