import requests
import dotenv
import os
dotenv.load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/354c60151bffcfc5fb8b6f35cc5c5dcc/flightDeals/prices"
        self.bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
