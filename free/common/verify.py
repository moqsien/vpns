# coding=UTF-8

VmessScheme = "vmess://"
VlessScheme = "vless://"
TrojanScheme = "trojan://"
ShadowSocksScheme = "ss://"
ShadowSocksRScheme = "ssr://"

def verify_content(content: str)->bool:
    if content.find("\xa1") > 0:
        return False
    if content.find("\xa0") >0:
        return False
    if content.find("127.0.0.1") > 0:
        return False
    if content.find("localhost") > 0:
        return False
    if content.find("[") > 0:
        return False
    # try:
    #     print(content)
    # except Exception as e:
    #     return False
    
    return any([content.startswith(VmessScheme),
            content.startswith(VlessScheme),
            content.startswith(TrojanScheme),
            content.startswith(ShadowSocksScheme),
            content.startswith(ShadowSocksRScheme)])
