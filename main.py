# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from sheety_manager import SheetyManager
from message_manager import MessageManager
import os
import json

load_dotenv()
flightsearch_apikey = os.getenv("flightsearch_apikey")
flightsearch_afillid = os.getenv("flightsearch_afillid")
date_from_to_search = (datetime.now() + timedelta(days=3)).strftime('%d/%m/%Y')
date_to_to_search = (datetime.now() + timedelta(days=93)).strftime('%d/%m/%Y')
# TODO: Получить информацию с Flight Search API с помощью объекта класса FlightSearch
flightsearch_url = 'https://tequila-api.kiwi.com/v2/search'
cities_to_visit = {'Paris': 'PAR',
                   'Berlin': 'BER',
                   'Tokyo': 'TYO',
                   'Sydney': 'SYD',
                   'Istanbul': 'IST',
                   'Kuala Lumpur': 'KUL',
                   'New York': 'NYC',
                   'San Francisco': 'SFO',
                   'Dakar': 'DKR',
                   'Cape Town': 'CPT'}

flightsearch = FlightSearch(apikey=flightsearch_apikey,
                            url=flightsearch_url)

# TODO: Обработать информацию, полученную от Flight Search API с помощью объекта класса FlightData
flight_info_list = []
for city, code in cities_to_visit.items():
    flightsearch_responce = flightsearch.make_request(fly_from='LED',
                                                      fly_to=code,
                                                      date_from=date_from_to_search,
                                                      date_to=date_to_to_search)
    flightdata = FlightData(flightsearch_responce)
    flight_info = flightdata.structure_the_flight_data()
    flight_info_list.append(flight_info)


# with open('json_files/fly_json.json', 'w') as fly_file:
#     json.dump(flight_info_list, fly_file, indent=4)

sheetymanager = SheetyManager()
# table_to_put = sheetymanager.get_new_table(flight_info_list)
sheetymanager.update_table(flight_info_list)
print(sheetymanager.cities_list_changed_price)
messagemanager = MessageManager()
for city in sheetymanager.cities_list_changed_price:
    for flight_info in flight_info_list:
        if flight_info["destination_city"] == city:
            messagemanager.send_sms(city_from=flight_info['departure_city'],
                                    city_from_iata=flight_info['departure_IATA_code'],
                                    city_to=flight_info['destination_city'],
                                    city_to_iata=flight_info["destination_IATA_code"],
                                    price=flight_info['flight_price'],
                                    date_from=flight_info['flight_dates'][0][4:14],
                                    date_to=flight_info['flight_dates'][1][4:14])
# TODO: Обновить данные в таблице Sheety в зависимости от ответа на запрос Flight Search API
#  помощью объекта класса DataManager

# получить данные о The SMS should include the departure airport IATA code, destination airport IATA code,
# departure city, destination city, flight price and flight dates
# TODO: В зависимости от изменения таблицы отправить SMS с помощью объекта класса NotificationManager
