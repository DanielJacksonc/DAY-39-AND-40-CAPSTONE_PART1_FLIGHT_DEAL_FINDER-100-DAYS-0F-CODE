import requests

from pprint import pprint
SHEETY_ENDPOINT = "https://api.sheety.co/c0ed83faf7679a0d5b046984251f886d/flightDealsProject/prices"
class DataManager:
    def __init__(self):
        self.destination_data = {}


#This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT)
        sheety_response.raise_for_status()
        result =sheety_response.json()
        self.destination_data = result["prices"]
        # pprint(result)

        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']

                }
            }
    #
            sheety_send = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(sheety_send.text)

