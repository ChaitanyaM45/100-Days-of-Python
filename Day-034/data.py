import requests

parameter={
    "amount":10,
    "type":"boolean",
}

data=requests.get(url="https://opentdb.com/api.php",params=parameter)

question_data = data.json()['results']
