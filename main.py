import requests
import time
import os

def send_alert(msg):
    tele_url = os.environ.get('TELE')
    formatted_msg = requests.utils.quote(msg)
    response = requests.get(tele_url + formatted_msg)
    if response.ok:
        print(response.json())
    else:
        print("ERROR:", response.json())


spinny_url = "https://api.spinny.com/sp-consumer-search/product/listing/?city=delhi,gurgaon,noida&product_type=cars&model=tiago&category=used&&page=1&availability=available"
response = requests.get(spinny_url)
if not response.ok:
    print("ERROR:", response.json())
else:
    data = response.json()
    prev_count = 0
    while True:
        count = data.get('count')
        if count != prev_count:
            send_alert("New Tiago available, Count: " + str(count))
        prev_count = count
        print(count)
        # @@@ change
        time.sleep(60 * 60)
