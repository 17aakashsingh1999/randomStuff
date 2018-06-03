import requests

data={'regno':'5858410','sno':'09025','cno':'5756','B2':'Submit'}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language':'en-US,en;q=0.5',
         'Accept-Encoding':'gzip, deflate',
         'Referer':'http://cbseresults.nic.in/class12zpq/Class12th18.htm',
         'Content-Type':'application/x-www-form-urlencoded',
         'Content-Length':'42',
         'Connection':'keep-alive',
         'Upgrade-Insecure-Requests':'1'}

url = 'http://192.168.0.119/'

r=requests.post(url,data=data,headers=headers)
print(r.content)