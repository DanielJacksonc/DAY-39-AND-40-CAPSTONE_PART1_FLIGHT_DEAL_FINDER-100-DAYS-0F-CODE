#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    pprint(sheet_data)

    data_manager.update_destination_codes()