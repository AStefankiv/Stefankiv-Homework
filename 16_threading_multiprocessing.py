import requests
import threading
import time

cities = [
    {"name": "Calgary", "latitude": 51.05, "longitude": -114.09},
    {"name": "Da Nang", "latitude": 16.07, "longitude": 108.22},
    {"name": "Nanchang", "latitude": 28.68, "longitude": 115.85},
    {"name": "Kyiv", "latitude": 50.45, "longitude": 30.52},
    {"name": "Ivano-Frankivsk", "latitude": 48.92, "longitude": 24.71}
]

def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={'latitude'}&longitude={'longitude'}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    temperature_list = data["hourly"]["temperature_2m"]
    avg_temperature = sum(temperature_list) / len(temperature_list)
    return (city, avg_temperature)

def get_average_temperatures():
    temperatures = []
    with threading.Lock():
        for city in cities:
            temperatures.append(get_weather(city))
    return temperatures

def get_hottest_city():
    temperatures = get_average_temperatures()
    hottest_city = max(temperatures]
    return hottest_city

start_time = time.time()
average_temperatures = get_average_temperatures()
hottest_city = get_hottest_city()
end_time = time.time()
print(f"Average temperatures: {average_temperatures}")
print(f"Hottest city: {hottest_city}")
print(f"Execution time: {end_time - start_time}")