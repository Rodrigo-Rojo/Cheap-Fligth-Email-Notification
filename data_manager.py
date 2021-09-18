from citys import city_list
import requests
from flight_search import FlightSearch


class DataManager:
    def __init__(self, flight_search):
        self.flight_search = flight_search
        self.city_index = 1

    def create_data(self):
        for index in range(0, 8):
            city = city_list[index]
            self.city_index += 1
            iata = self.flight_search.get_iata(city)
            flight_data = self.flight_search.get_flight_data()
            flight_data = flight_data.split()
            price = flight_data[0]
            duration = flight_data[1]
            link = flight_data[2]
            sheety_data = {
                "price": {
                    "city": city,
                    "iata": iata,
                    "price": price,
                    "duration": duration
                }
            }
            sheety_link = f"https://api.sheety.co/YOURSHEETYLINK/flightDeals/prices/{self.city_index}"
            res = requests.put(url=sheety_link, json=sheety_data)
            res.raise_for_status()
            print(res.json())
