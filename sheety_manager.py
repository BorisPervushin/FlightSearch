from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()


class SheetyManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        sheety_token = os.getenv('sheety_token')
        self.url = 'https://api.sheety.co/ca514d056d0e774572f3f45f1d4f1900/flightDeals/prices'
        self.header = header = {'Authorization': f'Bearer {sheety_token}'}
        self.cities_list_changed_price = []

    def get_current_table(self):
        response = requests.get(url=self.url, headers=self.header)
        return response.json()

    def update_table(self, new_data):
        current_table = self.get_current_table()
        for new_flight_data in new_data:
            for i, old_flight_data in enumerate(current_table['prices']):
                if new_flight_data["destination_city"] == old_flight_data['city']:
                    if new_flight_data["flight_price"] < old_flight_data['lowestPrice']:
                        print(old_flight_data['city'])
                        self.cities_list_changed_price.append(old_flight_data['city'])
                        print(self.cities_list_changed_price)
                        exit()

                        put_url = f'https://api.sheety.co/ca514d056d0e774572f3f45f1d4f1900/flightDeals/prices/{old_flight_data["id"]}'
                        body = {
                            'price': {
                                'city':  old_flight_data['city'],
                                'iataCode': old_flight_data['iataCode'],
                                'lowestPrice': new_flight_data["flight_price"],
                                'link': new_flight_data["link"],
                                'id': old_flight_data['id']
                            }
                        }
                        response = requests.put(url=put_url, json=body, headers=self.header)
                        response.raise_for_status()

