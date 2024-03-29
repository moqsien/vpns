# coding=UTF-8
import sys
sys.path.append(".")

from datetime import datetime
from free.common.proxy import set_proxy, SiteBase
from free.common.encrypt import decode_base64

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
            # FreeUrl("https://bulink.me/sub/q2kpq/vm"),
            FreeUrl("https://sub.nicevpn.top/long"),
            FreeUrl("https://sub.sharecentre.online/sub"),
            FreeUrl("https://sub.nicevpn.top/long"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ZywChannel/free/main/sub"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ermaozi01/free_clash_vpn/main/subscribe/v2ray.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/freefq/free/master/v2"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/vveg26/get_proxy/main/dist/v2ray.config.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/baip01/yhkj/main/v2ray"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/iosoledad/soledadys/main/Azure.Aws.vmess/Azure.Aws.QuantumultX/Azure.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/ts-sf/fly/main/v2"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/free18/v2ray/main/v2ray.txt"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/vless"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ss"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ssr"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all3"),
            FreeUrl("https://ghproxy.com/https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/v2"),
            FreeUrl("https://wanshanziwo.eu.org/vmess/sub?c=US"),
            FreeUrl("https://wanshanziwo.eu.org/ssr/sub"),
            FreeUrl("https://wanshanziwo.eu.org/sip002/sub"),
            FreeUrl("https://wanshanziwo.eu.org/trojan/sub"),
            # FreeUrl("https://ghproxy.com/"),
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
            # FreeUrl("https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub", True),
            # FreeUrl("https://raw.githubusercontent.com/freefq/free/master/v2", True),
            # FreeUrl("https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray", True),
            # FreeUrl("https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub", True),
            # FreeUrl("https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray", True),
            # FreeUrl("https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt", True),
            # FreeUrl("https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt", True),
            # FreeUrl("https://raw.githubusercontent.com/vveg26/get_proxy/main/dist/v2ray.config.txt", True),
            # FreeUrl("https://raw.githubusercontent.com/baip01/yhkj/main/v2ray", True),
            # FreeUrl("https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2", True)
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
                    r = str(decode_base64(content), "utf-8")
                    result += r
            except Exception as e:
                print(f"Download {freeurl.url} failed.")
                print(e)
        return result
    
    
if __name__ == "__main__":
    set_proxy("http://localhost:2019")
    s = SiteFreeSubscribes()
    r = s.parse()
    print(r.split("\n"))
