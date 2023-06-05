import base64
import io
import sys
import requests
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class SitCfmem:
    def __init__(self):
        self.url = "https://www.cfmem.com/search/label/free"
        
    def get_resp(self)->str:
        resp = requests.get(self.url)
        html = etree.HTML(resp.text)
        result = html.xpath('//h2[@class="entry-title"]/a/@href')
        if len(result) > 0:
            url = result[0]
            resp = requests.get(url)
            return resp.text
        return ""
            
    def parse(self)->str:
        content = self.get_resp()
        html = etree.HTML(content)
        result = html.xpath('//span[@role="presentation"]/text()')
        if len(result) > 0:
            return base64.b64decode(result[0]).decode('utf-8')
        return ""
    
    def url(self)->str:
        return self.url
        
if __name__ == '__main__':
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    s = SitCfmem()
    print(s.parse())
