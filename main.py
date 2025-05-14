#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import dotenv
import os
from pprint import pprint
import data_manager as dm
import flight_search as fs
d_m = dm.DataManager()

#d_m.load_data()
# d_m.data_holder = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#             {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#             {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
#             {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
#             {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
#             {'city': 'Kuala Lumpur',
#              'iataCode': '',
#              'id': 7,
#              'lowestPrice': 414},
#             {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
#             {'city': 'San Francisco',
#              'iataCode': '',
#              'id': 9,
#              'lowestPrice': 260},
#             {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]}
#
# sheet_data = d_m.data_holder
# for items in sheet_data["prices"]:
#     if items["iataCode"] == "":
#         items["iataCode"]= "TESTING"
# pprint(sheet_data)
new_fs = fs.FlightSearch()

iata = new_fs.get_iata_code_from_city("Paris")
pprint(iata)

