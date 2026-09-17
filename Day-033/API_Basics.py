import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code) #op:200 ie SUCCESS
response1=requests.get(url="http://api.open-notify.org/is-now.json") #invalid url
print(response1.status_code) #op:404 ie URL NOT FOUND

response.raise_for_status()
response1.raise_for_status()

data=response.json()
print(data)
print(data['iss_position'])
latitude=data['iss_position']['latitude']
longitude=data['iss_position']['longitude']

iss_position=(latitude,longitude)
print(iss_position)

MY_LAT=18.522892
MY_LONG=73.859622
DATE="2026-09-17"

parameter={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "date":DATE,
}

response2=requests.get(url="https://api.sunrise-sunset.org/v2",params=parameter)
print(response2.json()['sunrise'])
print(response2.json()['sunset'])