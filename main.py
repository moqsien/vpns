import sys
sys.path.append("..")
from vpns.sites.v2cross import SiteV2Cross

if __name__ == '__main__':
    s = SiteV2Cross()
    print(s.parse())
