# coding=UTF-8
from lxml import etree
from free.common.proxy import SiteBase

class SiteWenpBlog(SiteBase):
    def __init__(self):
        super(SiteWenpBlog, self).__init__()
        self.url = "https://www.wenpblog.com/list/5/1.html"
        
    def get_resp(self)->str:
        resp = self.request(self.url)
        html = etree.HTML(resp)
        result = html.xpath('//div[@class="list-pic-body"]//h3/a/@href')
        if len(result) > 0:
            url = result[0]
            resp = self.request(url)
            return resp
        return ""
    
    def parse(self)->str:
        print(f"processing {self.url}...")
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
    
    def __str__(self) -> str:
        return self.url

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    s = SiteWenpBlog()
    print(s.parse())
