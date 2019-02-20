import requests

api_key = 'ec3bce6e19143759ff04b29b9573de09'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
city_name = input("Please Enter your city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

print(response)
x = response.json()
print(x['wind']['speed'])