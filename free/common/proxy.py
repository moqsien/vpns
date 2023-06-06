# coding=UTF-8
import os
import chardet
import requests

VPNS_PROXY_ENV_NAME = "VPNS_DOWNLOAD_PROXY"

def get_proxy():
    p = os.environ.get(VPNS_PROXY_ENV_NAME, "")
    proxies = dict()
    if p != "":
        proxies["https"] = p
    return proxies

def set_proxy(p):
    os.environ.setdefault(VPNS_PROXY_ENV_NAME, p)

class SiteBase(object):
    def request(self, url:str, useproxy:bool=False, timeout:int=120) ->str:
        proxies = dict()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
        }
        if useproxy:
            proxies = get_proxy()
        try:
            resp = requests.get(url, timeout=timeout, proxies=proxies, headers=headers)
            return resp.text
        except Exception as e:
            print(f"Donwload [{url}] failed.")
            print(e)
        return ""
