import requests 
import json
#Inform user what the program is used for
print("This program will tell you the weather in any city in the US, UK, and CAN.")
#Prompt user for city or postal code
city = input("Enter a city or a postal code: ")
#call api with given city or postal code
response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=APIKEY&q={city}&aqi=no')
#Format response into json 
data = response.text
weatherData = json.loads(data)
#Display the temperature and the current weather
#i am adding 2 more apis to provide the most accurate details(Geocoding api and openweather api)
print(f"The weather in {weatherData['location']['name']}, {weatherData['location']['country']} is {weatherData['current']['condition']['text']}")
print(f"The temperature is {weatherData['current']['temp_c']}°C, feels like {weatherData['current']['feelslike_c']}°C")
