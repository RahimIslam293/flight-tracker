import requests
from pprint import pprint
import dotenv
import os

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

    def update_iata_code(self, city_name, iata_code) -> bool:
        updated = False
        if len(self.data_holder) == 0:
            self.load_data()
        for city_data in self.data_holder["prices"]:
            if city_data["city"].title() == city_name.title():
                city_data["iataCode"] = iata_code.upper()
                updated = True
        return updated
