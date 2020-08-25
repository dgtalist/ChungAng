import os
import sys
import urllib.request
import json

client_id = "p0wHZ6X3CxQNHHW7XLOu"
client_secret = "3LB5zIzngT"

with open('index.txt', 'r', encoding='utf8') as f:
    srcText = f.read()

encText = urllib.parse.quote(srcText)
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    pprint(res)

    with open('trans.txt', 'w', encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])

    #print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
