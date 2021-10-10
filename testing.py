from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

twilio_sid = os.getenv('twilio_sid')
twilio_token = os.getenv('twilio_token')
telephone_number_to = os.getenv('telephone_number_to')
telephone_number_from = os.getenv('telephone_number_from')
city_from = 'Saint-Petersburg'
city_from_iata = 'LED'
city_to = 'Paris'
city_to_iata = 'PAR'
price = 20
date_from = '2020-12-18'
date_to = '2020-12-21'
message_text = f'Low price alert! Only €{price} to fly from {city_from}-{city_from_iata} to {city_to}-{city_to_iata}, ' \
               f'from {date_from} to {date_to}'

client = Client(twilio_sid, twilio_token)

message = client.messages.create(
    to=telephone_number_to,
    from_=telephone_number_from,
    body=message_text
)
