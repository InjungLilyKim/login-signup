import requests
import random
import math

url = "http://api.reimaginebanking.com/merchants?key=7cf6b1d1e5478b6344582133572262a7"
merch_list = []
response = requests.get(url)
for merch in response.json():
    merch_list.append(merch["_id"])

url = "http://api.reimaginebanking.com/accounts/5a7e88376514d52c7774b0e4/purchases?key=7cf6b1d1e5478b6344582133572262a7"

for d in range(1):
    rand = random.randint(1,4812)
    response = requests.post(url, data={"merchant_id" : "59fe53e2b390353c953a1db4", "medium": "balance", "purchase_date": "2018-02-01","amount":'1', "status": "pending", "description": "-"})
    print(response.content)

for d in range(1):
    rand = random.randint(1,4812)
    response = requests.post(url, data={"merchant_id" : merch_list[rand], "medium": "balance", "purchase_date": str("2018-02-" + str(round(d+1,2))), "amount": 0, "status": "pending", "description": "-"})
    print(response.content)
    