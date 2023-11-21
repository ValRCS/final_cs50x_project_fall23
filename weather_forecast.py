# Let's make an application that asks for city name and 
# returns the weather forecast for the next 5 days.

# we will use the requests library to make a request to the weather API
# first we need to install it using pip
# Project page: https://pypi.org/project/requests/
# pip install requests
# once installed (need to install only once) we use it like this
import requests

# then we need an API key from https://openweathermap.org/api
# instead we will use API from https://open-meteo.com/

# we will use the requests library to make a request to the weather API

# let's save a dictionarythat hold cities and their latitudes and longitudes
# we will use this to get the weather forecast for the next 5 days
# first value is latitude and second is longitude
cities = {
    "Rome": (41.9028, 12.4964),
    "Rīga": (56.9496, 24.1052),
    "London": (51.5074, 0.1278),
    "Liepāja": (56.5110, 21.0136),
    "Paris": (48.8566, 2.3522),
    "Berlin": (52.5200, 13.4050),
}
DEFAULT_CITY = "Rīga"

# ask for city
city = input("Enter city name: ")
# check if city is in the dictionary
if city in cities:
    latitude, longitude = cities[city]
else:
    print(f"City not found using {DEFAULT_CITY} as default")
    latitude, longitude = cities[DEFAULT_CITY]

# make a request to the API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
# print the url
print(url)
# make the request
response = requests.get(url)

# print json response
print(response.json())

# let's print time and temperature for the next 5 days
# we will use the json response
# we will use a for loop to iterate over the list of forecasts
# we will iteratete over zip of both lists
# we will use f-strings to format the output
# let's also write to a csv file with two columsn time and temperature
# let's do it by hand first
# we want our file name to have current date and time and city name
# we will use datetime module
# https://docs.python.org/3/library/datetime.html

from datetime import datetime
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
file_name = f"{city}_{timestamp}.csv"

with open(file_name, "w", encoding="utf-8") as file:
    # write header
    file.write("Time,Temperature\n")
    for time,temperature in zip(response.json()["hourly"]["time"], response.json()["hourly"]["temperature_2m"]):
        print(f"Time: {time} Temperature: {temperature}°C")
        # write to file
        file.write(f"{time},{temperature}\n")
