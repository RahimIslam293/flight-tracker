import requests
from pprint import pprint
import dotenv
import os
import flight_search

dotenv.load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/354c60151bffcfc5fb8b6f35cc5c5dcc/flightDeals/prices"
        self.bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}
        self.data_holder = {}

    def load_data(self):
        resp = requests.get(url=self.endpoint, headers=self.headers)
        resp.raise_for_status()
        self.data_holder = resp.json()

    def update_sheety(self):
        for city_airports in self.data_holder["prices"]:
            update_endpoint = f"{self.endpoint}/{city_airports["id"]}"
            updated_set = {
                "price": city_airports
            }
            resp = requests.put(url=update_endpoint, json=updated_set, headers=self.headers)
            print(resp.json())
