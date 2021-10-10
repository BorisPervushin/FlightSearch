class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, json_data):
        self.data = json_data
        self.departure_IATA_code = self.data['data'][0]['flyFrom']  # the departure airport IATA code
        self.destination_IATA_code = self.data['data'][0]['cityCodeTo']  # destination airport IATA code

        self.departure_city = self.data['data'][0]['cityFrom']  # departure city,
        self.destination_city = self.data['data'][0]['cityTo']  # destination city,
        self.flight_price = self.data['data'][0]['price']  # flight price
        self.flight_dates = ['UTC ' + self.data['data'][0]['utc_departure'],
                             'UTC ' + self.data['data'][0]['utc_arrival']]  # flight dates
        self.link = self.data['data'][0]["deep_link"]

    def structure_the_flight_data(self):
        return {'departure_IATA_code': self.departure_IATA_code,
                'destination_IATA_code': self.destination_IATA_code,
                'departure_city': self.departure_city,
                'destination_city': self.destination_city,
                'flight_price': self.flight_price,
                'flight_dates': self.flight_dates,
                'link': self.link,
                }
