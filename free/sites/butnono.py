import sys
sys.path.append(".")

from free.common.proxy import set_proxy, SiteBase

class SiteButNoNo(SiteBase):
    def __init__(self):
        super(SiteButNoNo, self).__init__()
        self.urls:list = [
            "https://www.butnono.com/wp-content/uploads/2020/06/v2ray%E9%80%9A%E7%94%A8vmess%E8%8A%82%E7%82%B9.txt",
            "https://www.butnono.com/wp-content/uploads/2020/06/ssr%E8%8A%82%E7%82%B927%E4%B8%AA.txt",
        ]

    def get_resp(self, url:str)->str:
        return self.request(url=url)
    
    def parse(self)->str:
        result = ""
        for url in self.urls:
            print(f"processing {url}...")
            content = self.get_resp(url)
            result += content
        return result


if __name__ == "__main__":
    set_proxy("http://localhost:2019")
    s = SiteButNoNo()
    r = s.parse()
    print(r.split("\n"))
