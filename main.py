#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import dotenv
import os
from pprint import pprint
from flight_data import find_cheapest_flight
import flight_search as fs
import data_manager as dm
d_m = dm.DataManager()
new_fs = fs.FlightSearch()




d_m.load_data()


#iata = new_fs.get_iata_code_from_city("Paris")
# pprint(d_m.data_holder)

# for item in d_m.data_holder["prices"]:
#     iata = new_fs.get_iata_code_from_city(item["city"])
#     item["iataCode"] = iata
#
# d_m.update_sheety()

for locations in d_m.data_holder["prices"]:
    if locations["iataCode"] != "NOT FOUND":
        flight = new_fs.search_for_flights(locations["iataCode"],"2025-11-18","2025-11-25",1,"USD")
        find_cheapest_flight(flight_data=flight)


