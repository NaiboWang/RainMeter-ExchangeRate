from django.http import HttpResponse
import json,requests
from datetime import datetime
from threading import Timer

st = ""

def fetch():
    global st
    dt=datetime.utcnow().hour + 8
    if dt>9:
        url="http://web.juhe.cn:8080/finance/exchange/rmbquot?type=1&bank=&key=90f46fce44dade2b89d243980f5adfec"
        #url = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
        strhtml = requests.get(url)
        st = json.loads(strhtml.text)
        #print(st)
    t = Timer(900, fetch)
    t.start()

def get_time():
    return st["data"]["t"]

def get_rate(i=0,t=False):
    global st
    if t:
        url="http://web.juhe.cn:8080/finance/exchange/rmbquot?type=1&bank=&key=90f46fce44dade2b89d243980f5adfec"
        strhtml = requests.get(url)
        st = json.loads(strhtml.text)
    if i == 0:
        return st["result"][0]["新加坡元"]["bankConversionPri"]
    elif i == 1:
        return st["result"][0]["美元"]["bankConversionPri"]
    elif i == 2:
        return st["result"][0]["港币"]["bankConversionPri"]
    elif i == 3:
        return st["result"][0]["新加坡元"]["date"]
    else:
        return st["result"][0]["新加坡元"]["time"]

def hello(request):
    i = int(request.GET["i"])
    return HttpResponse(get_rate(i))

fetch()
