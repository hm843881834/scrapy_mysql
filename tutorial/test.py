from urllib import request
import re

response =  request.urlopen('http://proxysteward.sinaapp.com/api/get?key=43EF9FBE-56CA-4959-B919-35AD7C0C0DE9')
ipStr = response.read().decode()
ipStr = re.findall(r'"(.+)"',ipStr)[0]
print(ipStr)