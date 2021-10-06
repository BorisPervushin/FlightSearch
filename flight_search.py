import requests


# import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, apikey: str, url: str):
        self.header = {'apikey': apikey}
        self.url = url

    def make_request(self, fly_from: str, fly_to: str, date_from: str, date_to: str):
        parameters = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to,
        }

        response = requests.get(url=self.url, params=parameters, headers=self.header)
        response.raise_for_status()
        return response
        # with open('fly_info.json', 'w') as fly_file:
        #     json.dump(response.json(), fly_file, indent=4)
