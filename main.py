#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import dotenv
import os
import data_manager as dm
dotenv.load_dotenv()

d_m = dm.DataManager()

print(d_m.bearer_token)
print(d_m.headers)
print(d_m.endpoint)
d_m.load_data()

print(d_m.data_holder)
