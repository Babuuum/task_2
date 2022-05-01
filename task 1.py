import requests

URL =  "https://superheroapi.com/api/2619421814940190"
heroes = {"Captain America": 0, "Thanos": 0, "Hulk": 0}


for hero in heroes:
    response = requests.get(f"{URL}/search/{hero}")
    response.raise_for_status()
    if response.status_code == 200:
        heroes[hero] = response.json()["results"][0]["id"]
    else:
        print("Ошибка")
for hero in heroes:
    response = requests.get(f"{URL}/{heroes[hero]}/powerstats")
    response.raise_for_status()
    if response.status_code == 200:
        heroes[hero]= response.json()["intelligence"]

    else:
        print("Ошибка")
print(sorted(heroes)[-1])
