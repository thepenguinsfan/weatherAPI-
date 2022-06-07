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
print(f"The weather in {weatherData['location']['name']}, {weatherData['location']['country']} is {weatherData['current']['condition']['text']}")
print(f"The temperature is {weatherData['current']['temp_c']}°C, feels like {weatherData['current']['feelslike_c']}°C")
print(f"Do you want more information about {weatherData['location']['name']}? 1 for yes, 2 for no.")
userAnswer = int(input())
if userAnswer == 1:
  print(f"The humidity is {weatherData['current']['humidity']}%")
  print(f"The Wind speed is {weatherData['current']['wind_kph']} km/h with gusts of {weatherData['current']['gust_kph']} km/h")
  print(f"The UV is {weatherData['current']['uv']}")
else:
  print("Have a good day!")
