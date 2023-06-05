import io
import sys
import requests
from lxml import etree

class SiteMianfeifq:
    def __init__(self):
        self.url = "https://gitlab.com/mianfeifq/share/-/blob/master/README.md?format=json&viewer=rich"
        
    def get_resp(self)->str:
        resp = requests.get(self.url)
        json_resp = resp.json()
        html_str = json_resp["html"]
        return html_str
    
    def parse(self)->str:
        html_str = self.get_resp()
        html = etree.HTML(html_str)
        result = html.xpath("//code/span/text()")
        return "\n".join(result)
    
    def url(self)->str:
        return self.url
    
if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    s = SiteMianfeifq()
    print(s.parse())
