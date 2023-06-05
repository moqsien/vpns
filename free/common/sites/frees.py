# coding=UTF-8
import sys
sys.path.append("..")

import base64
from datetime import datetime
from free.common.proxy import set_proxy, SiteBase

class FreeUrl:
    def __init__(self, url:str, use_proxy: bool=False):
        self.url:str = url
        self.proxy:bool = use_proxy
        
    def __str__(self) -> str:
        return self.url

class SiteFreeSubscribes(SiteBase):
    def __init__(self):
        super(SiteFreeSubscribes, self).__init__()
        date_str = datetime.now().strftime("%Y/%m/%Y%m%d")
        self.urls = [
            FreeUrl("https://bulink.me/sub/q2kpq/vm"),
            FreeUrl("https://raw.fastgit.org/freefq/free/master/v2"),
            FreeUrl("https://sub.nicevpn.top/long"),
            FreeUrl("https://raw.fastgit.org/Pawdroid/Free-servers/main/sub"),
            FreeUrl("https://sub.sharecentre.online/sub"),
            FreeUrl(f"https://clashnode.com/wp-content/uploads/{date_str}.txt"),
            FreeUrl(f"https://nodefree.org/dy/{date_str}.txt"),
            FreeUrl(f"https://hiclash.com/wp-content/uploads/{date_str}.txt"),
            FreeUrl(f"https://wefound.cc/freenode/{date_str}.txt"),
            FreeUrl("https://api.subcloud.xyz/sub?target=v2ray&url=https%3A%2F%2Fraw.githubusercontent.com%2Fssrsub%2Fssr%2Fmaster%2FSurge.conf"),
            FreeUrl("https://api.subcloud.xyz/sub?target=v2ray&url=https%3A%2F%2Fraw.githubusercontent.com%2Fssrsub%2Fssr%2Fmaster%2FClash.yml"),
            FreeUrl("https://api.subcloud.xyz/sub?target=v2ray&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fzyzmzyz%2Ffree-nodes%40master%2FClash.yml&insert=false"),
            FreeUrl("https://api.subcloud.xyz/sub?target=v2ray&url=https%3A%2F%2Fcdn.statically.io%2Fgh%2Fopenrunner%2Fclash-freenode%2Fmain%2Fclash.yaml&insert=false"),
            FreeUrl("https://freefq.neocities.org/free.txt"),
            FreeUrl("https://gitlab.com/api/v4/projects/36060645/repository/files/data%2Fv2ray%2FtvNUi5rjr.txt/raw?ref=main&private_token=glpat-iC4t7zq8nsV2xKYseBfU"),
            FreeUrl("https://tt.vg/ZlJdd", True),
            FreeUrl("https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray", True),
            FreeUrl("https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub", True),
            FreeUrl("https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray", True),
            FreeUrl("https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt", True),
            FreeUrl("https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt", True),
            FreeUrl("https://raw.githubusercontent.com/vveg26/get_proxy/main/dist/v2ray.config.txt", True),
            FreeUrl("https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2", True)
        ]
    
    def get_resp(self, freeurl:FreeUrl)->str:
        return self.request(freeurl.url, freeurl.proxy)
    
    def parse(self)->str:
        result = ""
        for freeurl in self.urls:
            print(f"processing {freeurl.url}...")
            content = self.get_resp(freeurl)
            try:
                if content:
                    r = str(base64.b64decode(content), "utf-8")
                    result += r
                    # print(r)
            except Exception as e:
                print(f"Download {freeurl.url} failed.")
                print(e)
        return result
    
    
if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    set_proxy("http://localhost:2019")
    s = SiteFreeSubscribes()
    s.parse()
    # print(s.parse())
