import requests

town = input("Выберите город: ")
url = f"https://wttr.in/{town}"

params = {
    "nMm": "" ,
    "lang" : "ru"
}

response = requests.get(url, params=params)
response.raise_for_status()
print(response.text)