import requests,urllib
from bs4 import BeautifulSoup

url = "http://detik.com"

r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.text,"html.parser")
    img = soup.find_all("img")
    total_image = len(img)
    total_size = 0

    for a in img:
        src = a.get('src')
        if src.startswith("//"):
            src = "http:" + src
        elif src.startswith("http"):
            src = src
        else:
            src = url + "/" + src

        file = urllib.urlopen(src)
        size = file.headers.get("content-length")
        file.close()
        total_size += int(size)

    print "Total Image : %d" % total_image
    print "Total Size : %d" % total_size
else:
    print "Tidak bisa mengakses detik.com"
