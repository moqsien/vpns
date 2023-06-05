import io
import sys
import requests
from lxml import etree

class SiteWenpBlog:
    def __init__(self):
        self.url = "https://www.wenpblog.com/list/5/1.html"
        
    def get_resp(self)->str:
        resp = requests.get(self.url)
        html = etree.HTML(resp.text)
        result = html.xpath('//div[@class="list-pic-body"]//h3/a/@href')
        if len(result) > 0:
            url = result[0]
            resp = requests.get(url)
            return resp.content.decode("utf-8")
        return ""
    
    def parse(self)->str:
        content = self.get_resp()
        html = etree.HTML(content)
        result = html.xpath('//blockquote//text()')
        r = ""
        for line in result:
            if line.endswith("\n"):
                r += line
        return r.rstrip("\n")
    
    def url(self)->str:
        return self.url

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    s = SiteWenpBlog()
    print(s.parse())
