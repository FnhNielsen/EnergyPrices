import requests
from datetime import date

from fastapi import FastAPI

app = FastAPI()

def compose_url():
    url = "https://api.energidataservice.dk/dataset/Elspotprices?offset=0&filter={%22PriceArea%22:%22DK1%22}&sort=HourUTC%20DESC&timezone=dk"
    return url

@app.get("/")
async def get_prices():
    payload = []
    data = {}
    try:
        api = requests.get(compose_url()).json()
        for i in api["records"]:
            data = {"HourDK": i["HourDK"],"Area": i["PriceArea"], "Spot price": i["SpotPriceDKK"]/100}
            payload.append(data)
            print(payload)
    except Exception as ex:
        raise Exception(str(ex))
    return payload

if __name__ == "__main__":
    get_prices()