import requests

def get_coordinates(city):
    geocoding_url = f"https://api.open-meteo.com/v1/geocode?city={city}"
    response = requests.get(geocoding_url)
    data = response.json()
    if "error" in data:
        raise Exception(f"Error: {data['error']}")
    latitude = data["latitude"]
    longitude = data["longitude"]
    return latitude, longitude

# Function to fetch the current weather data for given coordinates
def get_weather(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    response = requests.get(weather_url)
    data = response.json()
    return data

# Main program
city = input("Enter the name of the city: ")
latitude, longitude = get_coordinates(city)
weather_data = get_weather(latitude, longitude)

# Extract relevant information from the weather data
temperature = weather_data["current"]["temperature"]
humidity = weather_data["current"]["humidity"]
wind_speed = weather_data["current"]["wind_speed"]
wind_direction = weather_data["current"]["wind_direction"]

# Print the weather information
print(f"Weather in {city}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Wind Direction: {wind_direction}°")