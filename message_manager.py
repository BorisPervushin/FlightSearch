from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


class MessageManager:
    def __init__(self):
        self.twilio_sid = os.getenv('twilio_sid')
        self.twilio_token = os.getenv('twilio_token')
        self.telephone_number_to = os.getenv('telephone_number_to')
        self.telephone_number_from = os.getenv('telephone_number_from')

    def send_sms(self, city_from, city_from_iata, city_to, city_to_iata, price, date_from, date_to):
        message_text = f'Low price alert! Only €{price} to fly from {city_from}-{city_from_iata} to {city_to}-{city_to_iata}, ' \
                       f'from {date_from} to {date_to}'

        client = Client(self.twilio_sid, self.twilio_token)

        message = client.messages.create(
            to=self.telephone_number_to,
            from_=self.telephone_number_from,
            body=message_text
        )
