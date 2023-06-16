import sys
sys.path.append(".")

from free.common.proxy import set_proxy, SiteBase
from free.common.encrypt import decode_base64
from lxml import etree

class SiteGetFreeNode(SiteBase):
    def __init__(self):
        super(SiteGetFreeNode, self).__init__()
        self.url = "https://getafreenode.com/"

    def get_resp(self, url:str)->str:
        resp = self.request(url=url)
        html = etree.HTML(resp)
        url = html.xpath("//a[1]/@href")
        if len(url) > 0:
            url = url[0]
            resp = self.request(url=url)
            html = etree.HTML(resp)
            url = html.xpath('//button[@id="copySubscription"]/@value')
            if len(url) > 0:
                resp = self.request(url=url[0])
                return resp
        return ""
    
    def parse(self)->str:
        result = ""
        resp = self.get_resp(self.url)
        result = decode_base64(resp).decode("utf-8")
        return result.strip("\n")


if __name__ == "__main__":
    set_proxy("http://localhost:2019")
    s = SiteGetFreeNode()
    r = s.parse()
    print(r.split("\n"))
