VmessScheme = "vmess://"
VlessScheme = "vless://"
TrojanScheme = "trojan://"
ShadowSocksScheme = "ss://"
ShadowSocksRScheme = "ssr://"

def verify_content(content: str)->bool:
    return any([content.startswith(VmessScheme),
            content.startswith(VlessScheme),
            content.startswith(TrojanScheme),
            content.startswith(ShadowSocksScheme),
            content.startswith(ShadowSocksRScheme)])
