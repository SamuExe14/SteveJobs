# 1) 
try:
   with open("./res/file.txt", "w") as file:
      for _ in range(3):
         frase = input("Inserire una frase da scrivere su file: ")
         file.write(frase)
except FileNotFoundError:
   print("File o directory non esistente")
except Exception as _:
   print("Errore generico: ", _)

# 2)
try:
   with open("./res/dati_inesistenti.py", "r") as file:
      print("File trovato")
except FileNotFoundError:
   print("File o directory non esistente")
   
# 3)
import json

dizionario = {
   "Nome" : "Samuele",
   "Cognome" : "Leonardi",
   "Eta" : 21
}

try:
   with open("./res/infos.json", "w") as file:
      json.dump(dizionario, file, indent=4)
      file.close()
except FileNotFoundError:
   print("File non trovato")
