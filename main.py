#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import dotenv
import os
from pprint import pprint
import data_manager as dm
import flight_search as fs
d_m = dm.DataManager()
new_fs = fs.FlightSearch()

d_m.load_data()


#iata = new_fs.get_iata_code_from_city("Paris")
# pprint(d_m.data_holder)

for item in d_m.data_holder["prices"]:
    iata = new_fs.get_iata_code_from_city(item["city"])
    item["iataCode"] = iata

d_m.update_sheety()

