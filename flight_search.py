import requests
from pprint import pprint
import dotenv
import os

dotenv.load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_locations_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
        self.api_token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_APP_SECRET")
        self.oath_token = os.getenv("AMADEUS_OATH_BEARER_TOKEN")

    def refresh_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        print(body)
        resp = requests.post(url=self.api_token_endpoint, headers=headers, data=body)
        resp.raise_for_status()
        token_resp = resp.json()
        self.oath_token = token_resp["access_token"] # set oath token of class
        os.environ["AMADEUS_OATH_BEARER_TOKEN"] = self.oath_token # set env variable to the new token
        dotenv.set_key(".env","AMADEUS_OATH_BEARER_TOKEN",os.environ["AMADEUS_OATH_BEARER_TOKEN"]) #update env file


    def get_iata_code_from_city(self, city):
        subtype = ["AIRPORT"]
        keyword = city
        view = "LIGHT"
        parameters = {
            "subType": subtype,
            "keyword": keyword,
            "page[limit]": 1,
            "view": view
        }
        headers = {"Authorization": f"Bearer {self.oath_token}"}
        iata_code = ""
        try:
            resp = requests.get(url=self.api_locations_endpoint, headers=headers, params=parameters)
            payload = resp.json()
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                print("Token Expired: Running get_token()")
                self.refresh_token()
                print("Token Updated")
                return self.get_iata_code_from_city(city)
            else:
                print(f"An HTTP error occurred: {e}")
        else:
            if payload["meta"]["count"] != 0:
                iata_code = payload["data"][0]["iataCode"]
            else:
                iata_code = "NOT FOUND"

        return iata_code
