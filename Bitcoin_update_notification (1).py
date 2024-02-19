import requests
import time
from datetime import datetime
ifttt_url = "https://maker.ifttt.com/trigger/{}/with/key/jLkEFSP8szyde8RUetnsmOww4C0KMJClFF3u73gpI3a"
website = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=9f3bb497-bfa0-40e0-9f1e-3d224d653eea'
response2 = requests.get(website)
response = response2.json()

def get_latest_bitcoin_price():
    #response2 = requests.get(website)
    #response = response2.json()
    name = response["data"][0]["name"]
    price = response["data"][0]["quote"]["USD"]["price"]
    return(str(price)[0:8])
print(type(get_latest_bitcoin_price()))

def ifttt_webhook(event,value):
    data = {"value1": value}
    ifttt_hook = ifttt_url.format(event)
    requests.post(ifttt_hook, json=data)
    
ifttt_webhook("Bitcoin_update", get_latest_bitcoin_price())

##date = str(datetime.now())
##time = date[11:19]
##seconds = time[6:8]
##print(seconds)
import time

def main():
    import time
    
    while True:
        price = get_latest_bitcoin_price()
        date = str(datetime.now())
        time = date[11:19]
        seconds = time[6:8]
        break
        if time == "00":
                ifttt_webhook("Bitcoin_update", get_latest_bitcoin_price)

main()
print(3)

