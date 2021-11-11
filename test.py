import requests
import json

securePasswordGeneratorAPI = "https://gm4gi7dzoh.execute-api.ap-northeast-2.amazonaws.com/dev"
data = {
    "env": "dev"
}
response = requests.post(securePasswordGeneratorAPI, json.dumps(data))
resp = json.loads(response.content)
strreturn = resp["body"]
print(strreturn)