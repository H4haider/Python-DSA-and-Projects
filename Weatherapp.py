import requests
import json

while(1):
  city = input("Enter the name of City or X to exit program: ")
  if(city=='x' or city=='X'):
    print("Exiting Program")
    break
  url = f"https://api.weatherstack.com/current?access_key=2ce56142f0f7b7191dc524e40e3f7151&query={city}"
  req = requests.get(url)
  data = json.loads(req.text)
  print("Temperature: ", data['current']['temperature'])
  print("Description: ", data['current']['weather_descriptions'])
  print("Humidity: ", data['current']['humidity'])
  print("Pressure: ", data['current']['pressure'])
  print("Wind Speed: ", data['current']['wind_speed'])
  print("Wind Direction: ", data['current']['wind_dir'])
