# we will download weather data from the internet and visualize it
# we need to find a website that provides weather data

# we will use datetime module
# datetime module documentation: https://docs.python.org/3/library/datetime.html
from datetime import datetime

# we will use https://api.open-meteo.com/ to get weather data
# we will use the requests library to make a request to the weather API
# request library documentation: https://docs.python-requests.org/en/master/
# first we need to install it using pip
# pip install requests in terminal - only once
import requests # now I can use the requests library

# first value is latitude and second is longitude
# these could have been read from another API or from a file or database
# so cities is a dictionary that holds cities and their latitudes and longitudes
cities = {
    "Rome": (41.9028, 12.4964),
    "Rīga": (56.9496, 24.1052),
    "London": (51.5074, 0.1278),
    "Liepāja": (56.5110, 21.0136),
    "Paris": (48.8566, 2.3522),
    "Berlin": (52.5200, 13.4050),
    "New York": (40.7128, -74.0060),
    "Tallinn": (59.4369, 24.7536),
    "Oslo": (59.9139, 10.7522),
    "Jūrmala": (56.9680, 23.7703),
}
DEFAULT_CITY = "Rīga"

# ask user for city and use default if not found
city = input("Enter city name: ")
# check if city is in the dictionary
if city not in cities:
    print(f"City not found using {DEFAULT_CITY} as default")
    city = DEFAULT_CITY

latitude, longitude = cities[city] # unpack tuple assign to two variables


# print latitude and longitude for testing
print(f"Latitude: {latitude} and longitude: {longitude}")

# now we need to create a URL to make a request to the API
# we need to pass latitude and longitude to the URL
# we will use f-string to format the URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
# alternative for wind and humidity: "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
# print the url
print(f"Will request data from: {url}")

# make the request
response = requests.get(url)
# we can check if we got 200 OK response
# list of HTTP status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code == 200:
    print("Success!")
else:
    print(f"Error: {response.status_code}")
    # we could quit program here or try again

# print json response - since we know this is a JSON API
# JSON stands for JavaScript Object Notation
# JSON org website: https://www.json.org/json-en.html
print(response.json())

# let's also save the time and temperatue to a .csv file
# we will use a timestamp and city as file name

timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
file_name = f"{timestamp}_{city}.csv"
print("Will save to {file_name}")

# let's open the file for writing
# we will use a context manager with
# file will be closed automatically
with open(file_name, mode="w", encoding="utf-8") as file:
    # let's write the header
    file.write("time,temperature\n")
    # let's write the data
    # we will use a for loop to iterate over the list of forecasts
    # we will iteratete over zip of both lists
    # we will use f-strings to format the output
    for time,temperature in zip(response.json()["hourly"]["time"], response.json()["hourly"]["temperature_2m"]):
        file.write(f"{time},{temperature}\n")
        # for debugging let's also print the data could comment out later
        # print(f"Time: {time} Temperature: {temperature}°C")
# here file is automatically closed

# let's print time and temperature for the next 5 days
# for time,temperature in zip(response.json()["hourly"]["time"], response.json()["hourly"]["temperature_2m"]):
#             print(f"Time: {time} Temperature: {temperature}°C")

# now I want to visualize temperature data vs time
# i will use matplotlib library
# if I don't have it installed I need to install it using pip
# pip install matplotlib in terminal - only once
# matplotlib documentation: https://matplotlib.org/stable/contents.html

# lets import pyplot from matplotlib
import matplotlib.pyplot as plt # notice we rename it to plt very common

# now I need two lists one for time and one for temperature
times = response.json()["hourly"]["time"]
temperatures = response.json()["hourly"]["temperature_2m"]
# let's print the lists
print(f"Times: {times}")
print(f"Temperatures: {temperatures}")

# let's plot the data
plt.plot(times, temperatures)
# let's add labels
plt.xlabel("Time")
plt.ylabel("Temperature")
# let's add title
plt.title(f"Temperature in {city}")
# i can save it to a file
plt.savefig(f"{timestamp}_{city}.png")
# let's show the plot in a window instead of saving it to a file
plt.show() # this will block the program until we close the window

