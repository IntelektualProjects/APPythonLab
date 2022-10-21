from bs4 import BeautifulSoup
import requests


url = "https://newtownps.powerschool.com/public/home.html"
username = "PotnuruS"
pswrd = "4349389"

headers = {
    "Cookie": "incap_ses_1347_2308459=8c2tNSd9C03u2H/1eIGxEv+FKGAAAAAAEjOBfs9FazPyhVH5GSZADA==; "
              "visid_incap_2308459=I+YB6eH2Tc60iKLXR9mwlv+FKGAAAAAAQUIPAAAAAAB+c8S4Ik/l5sszCYl+fDW2; "
              "BIGipServernewtownps_pool=1336022700.20480.0000; JSESSIONID=4791AD12359457A99FD38A7662EE8088",
    "Content-Length": 0,
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
data = {
    "account": "PotnuruS",
    "pw": "4349389"
}
r = requests.Session()
r.post(url, data=data)
