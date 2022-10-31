
#api call
import requests

response = requests.get("https://api.dev.doggly.co.kr/v1/public/product?limit=10000")

import json

datas = json.loads(response.text)

for i in range(len(datas)):

    if '[까이에슈슈] 와이드 프릴칼라 트위드자켓' == datas[i].get("product_name"):

        response_detail = requests.get("https://api.dev.doggly.co.kr/v1/public/product/detail/" + datas[i].get("product_uuid") + "?limit=10000")
        
        datas_detail = json.loads(response_detail.text)

        print(datas[i].get("product_uuid"))

        print(datas_detail[0])

