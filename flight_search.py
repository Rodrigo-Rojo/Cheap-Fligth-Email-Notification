import requests
import datetime as dt
KIWI_KEY = "YOURKEY"
KIWI_URL = "https://tequila-api.kiwi.com/v2/search"
KIWI_URL_LOCATIONS = "https://tequila-api.kiwi.com/locations/query"
today = dt.datetime.today()
month_after = dt.date.today() + dt.timedelta(days=180)
wiki_header = {
    "apikey": "YOURKEY"
}

class FlightSearch:
    def __init__(self):
        self.today = dt.datetime.today()
        self.month_after = dt.date.today() + dt.timedelta(days=120)
        self.flight = ""
        self.iata_code = ""
        self.wiki_params = {
        }
        self.flight_list = []

    def get_iata(self, city):
        res = requests.get(url=KIWI_URL_LOCATIONS, params={"term": city}, headers=wiki_header)
        res.raise_for_status()
        data = res.json()
        self.iata_code = data["locations"][0]["code"]
        return self.iata_code

    def get_flight_data(self):
        self.wiki_params = {
            "curr": "USD",
            "fly_from": "IDA",
            "fly_to": self.iata_code,
            "max_fly_duration": 20,
            "one_per_date": 1,
            "date_to": month_after.strftime("%d/%m/%Y"),
            "date_from": today.strftime("%d/%m/%Y"),
            "flight_type": "oneway"
        }
        res = requests.get(url=KIWI_URL, params=self.wiki_params, headers=wiki_header)
        res.raise_for_status()
        data = res.json()["data"]
        length = len(data[0]["route"])
        departure_date = data[0]['route'][0]['local_departure'].split("T")[0]
        arrive_date = data[0]['route'][length - 1]['local_arrival'].split("T")[0]
        arrive_hour = data[0]['route'][length - 1]['local_arrival'].split("T")[1].split(".")[0]
        departure_hour = data[0]['route'][0]['local_departure'].split("T")[1].split(".")[0]
        price = data[0]["price"]
        city_to = data[0]["cityTo"]
        duration = data[0]["duration"]['departure']
        link = data[0]["deep_link"]
        self.flight = f"For only ${price}, fly from IF to {city_to} Flight date: {departure_date} - {arrive_hour}" \
                      f" and Arrives at {arrive_date} - {departure_hour}\n"
        self.flight_list.append(self.flight)

        return f"{price} {round(duration / 60 / 60, 2)} {link}"

    def get_flight_str(self):
        return self.flight_list
