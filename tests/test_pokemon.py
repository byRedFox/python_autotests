# import pytest не использовался в заданиях домашки :()
import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b5e3ff0891f8ebbfd981d4460723c984"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "36135"
QUARY_PARAMS = {"trainer_id": "36135"}


def test_status_code():
    response = requests.get(url=f"{URL}/pokemons", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200


def test_name_my_trainer():
    my_trainer_name = requests.get(url=f"{URL}/trainers", headers=HEADER, params=QUARY_PARAMS)
    trainer_name = my_trainer_name.json()["data"][0]["trainer_name"]
    assert trainer_name == "Python"
