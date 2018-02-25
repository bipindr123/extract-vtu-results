from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re

f = "1bg15cs"

url = 'http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php' # Set destination URL here
 # Set POST fields here
name = "MIJAR"
i = 1
for i in range(0,200):
    myusn = f + '{num:03d}'.format(num=i)
    post_fields = {'usn': myusn}
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    res = re.findall(r"<b>:</b> (.+)<",json)
    print(res)
    print(myusn)
    if name in res.__str__():
        print(myusn)
        print("yay")

print(res)



#print(json)
