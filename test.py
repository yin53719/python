import requests
import json

payload={
    "key1":"aaaaa"
}
r=requests.post("http://httpbin.org/get",data=json.dumps(payload))

print(r.text)