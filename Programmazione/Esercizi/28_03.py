import json

dati = {"Nome": "Samuele",
        "Età" : 20,
        "Corso": "35"
        }

with open("studenti.json", "w") as file:
#   dati = json.load(file.read)
  json.dump(dati, file, indent=4) 
  
with open ("studenti.json", "r") as loader:
  new_dati = json.load(loader)
  print(new_dati)

dati["Curricula"] = "CyberSecurity"

with open("studenti.json","w") as my_file:
  json.dump(dati, my_file, indent=4)
  