import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")

HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
request_body = {"name": "generate", "photo_id": -1}
request_body_for_change_name = {"pokemon_id": "287015", "name": "finik", "photo_id": 391}
request_catch_pokemon = {"pokemon_id": "290718"}
query_params = {"trainer_id": "36135"}

responce_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=request_body)
print(responce_create.json())

chenge_pokemon_name = requests.put(
    url=f"{URL}/pokemons", headers=HEADER, json=request_body_for_change_name
)
print(chenge_pokemon_name.json())

catch_pokemon = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=request_catch_pokemon
)
print(catch_pokemon.json())

trainers_list = requests.get(url=f"{URL}/trainers", headers=HEADER, params=query_params)

print(trainers_list.json())
