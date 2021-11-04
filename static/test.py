import requests,json


s = requests.session()
url = "http://www.in-sight.cn:6061/ords/ws001/dp/customer_info"
r = s.get(url)
result = r.json()['items']
xmgk_z = []
for item in result:
        dict = {
                'customer_address': item.get("customer_address"),
                'customer_industry': item.get("customer_industry"),
                'customer_name': item.get("customer_name")
        }
        xmgk_z.append(dict)

xmgk_dirt = {
        "rows": xmgk_z
}

print(xmgk_dirt)

