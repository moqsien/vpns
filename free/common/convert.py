# coding=UTF-8
import yaml
import requests

def convert_clash_to_v2ray(content:str)->str:
    content.replace("\U0001f1fa", "", -1)
    y = yaml.load(content, Loader=yaml.FullLoader)
    for p in y["proxies"]:
        print(p["server"])


if __name__ == "__main__":
    resp = requests.get("https://raw.githubusercontent.com/ssrsub/ssr/master/Clash.yml", proxies={"https":"http://localhost:2019"})
    convert_clash_to_v2ray(resp.content.decode("utf-8"))
