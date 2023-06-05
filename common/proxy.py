import os

VPNS_PROXY_ENV_NAME = "VPNS_DOWNLOAD_PROXY"

def get_proxy():
    p = os.environ.get(VPNS_PROXY_ENV_NAME, "")
    proxies = dict()
    if p != "":
        proxies["https"] = p
    return proxies

def set_proxy(p):
    os.environ.setdefault(VPNS_PROXY_ENV_NAME, p)
