# coding:utf-8
from urllib import request
from urllib import parse

url = "http://db.auto.sohu.com/api/newSales/model?modelIds=1571&section=0"
data = {"id": "wdb", "pwd": "wdb"}

params = "?"
for key in data:
    params = params + key + "=" + data[key] + "&"
print("Get方法参数：" + params)

headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.1.2.151/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'

}

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)  # POST方法
# req = request.Request(url+params)  # GET方法
page = request.urlopen(req).read()
page = page.decode('utf-8')

print(page)