import requests
import threading
import time

def get_weather(city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": city["latitude"], "longitude": city["longitude"], "hourly": "temperature_2m"}
    response = requests.get(url, params=params)
    data = response.json()
    temperature_list = data["hourly"]["temperature_2m"]
    average_temperature = sum(temperature_list) / len(temperature_list)
    return city["name"], average_temperature

def get_temperature(city_data):
    return city_data[1]

def multi_thread():
    cities = [
        {"name": "Calgary", "latitude": 51.05, "longitude": -114.09},
        {"name": "Da Nang", "latitude": 16.07, "longitude": 108.22},
        {"name": "Nanchang", "latitude": 28.68, "longitude": 115.85},
        {"name": "Kyiv", "latitude": 50.45, "longitude": 30.52},
        {"name": "Ivano-Frankivsk", "latitude": 48.92, "longitude": 24.71}
    ]
    result = []

    def request(city):
        print(f"Start of {city['name']}")
        result.append(get_weather(city))
        print(f"End of {city['name']}")

    thread_list = []
    for city in cities:
        thread = threading.Thread(target=request, args=(city,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    hottest_city = max(result, key=get_temperature)
    print(f"The hottest city is {hottest_city[0]} with a temperature of {hottest_city[1]}°C")

if __name__ == "__main__":
    start = time.time()
    multi_thread()
    print(f"Program ended in {time.time() - start}")

####################################################################

import requests
from multiprocessing import Process
import time

def get_weather(city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": city["latitude"], "longitude": city["longitude"], "hourly": "temperature_2m"}
    response = requests.get(url, params=params)
    data = response.json()
    temperature_list = data["hourly"]["temperature_2m"]
    average_temperature = sum(temperature_list) / len(temperature_list)
    return city["name"], average_temperature

def get_temperature(city_data):
    return city_data[1]

def multi_process():
    cities = [
        {"name": "Calgary", "latitude": 51.05, "longitude": -114.09},
        {"name": "Da Nang", "latitude": 16.07, "longitude": 108.22},
        {"name": "Nanchang", "latitude": 28.68, "longitude": 115.85},
        {"name": "Kyiv", "latitude": 50.45, "longitude": 30.52},
        {"name": "Ivano-Frankivsk", "latitude": 48.92, "longitude": 24.71}
    ]
    result = []

    def request(city):
        print(f"Start of {city['name']}")
        result.append(get_weather(city))
        print(f"End of {city['name']}")

    process_list = []
    for city in cities:
        process = Process(target=request, args=(city,))
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()

    hottest_city = max(result, key=get_temperature)
    print(f"The hottest city is {hottest_city[0]} with a temperature of {hottest_city[1]}°C")

if __name__ == "__main__":
    start = time.time()
    multi_process()
    print(f"Program ended in {time.time() - start}")