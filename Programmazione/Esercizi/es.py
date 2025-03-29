import csv
import json

with open("/home/samu/Desktop/SteveJobs/Programmazione/Esercizi/res/file.csv", "r", newline="") as csvfile:
   content = csv.reader(csvfile)
   for riga in content:
      dizionario = {f"{riga}"}
      print(f"{dizionario}")
   # with open("./res/studenti.json", "w") as json_file:
   #    json.dump(dizionario, json_file, indent=4)
