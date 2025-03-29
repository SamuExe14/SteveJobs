
#! JSON
import json

dati = {"Nome": "Alice", "età": 28, "Città": "Firenze"}

with open("config.json", "r") as file:
	dati = json.load

with open("config.json", "w") as file:
	json.dump(dati, file, indent=4)