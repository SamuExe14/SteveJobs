
#! MODULI PERSONALIZZATI

import libs.modulo_blocco5 as mm
from libs.modulo_blocco5 import saluta, Calcolatore

print(mm.saluta("Samuele")) # uso del modulo con alias
print(saluta("Samuele"))
calc = Calcolatore()

print(calc.somma(3,4))

#! FILE 

file = open("res/dati.txt", "r") # r per aprire il file in modalità read
contenuto = file.read()
file.close() # è fondamentale chiudere il file per liberare risorse e la rimozione dei lock
print(contenuto)

file = open("./res/dati.txt", "w") # w per aprire in modalità write(sovrascrive il contenuto)
file.write("Hello World!")
file.close()

with open("./res/dati.txt","r") as f:
   print(f.read())
   f.close()

#! GESTIONE DELLE ECCEZIONI

a = input("Inserire un numero: ")
try:
   b = int(a)
except Exception as _:
   print("Si è verificato un errore: ", _)

try:
   risultato = 10/2
except ZeroDivisionError:
   print("Non è possibile effettuare una divisione per zero")
else: # la clausola else viene eseguita se non si verificano eccezioni
   print("Risultato:", risultato)

#? ESEMPIO ECCEZIONE CON I FILE

try:
   file = open("./res/dati.txt", "r")
   contenuto = file.read()
except FileNotFoundError:
   print("Il file non è stato trovato")
except Exception as _:
   print("Errore generico: ", _)
finally:
   if 'file' in locals():
      file.close() # in qualsiasi caso chiude il file

file = open("./res/dati.txt", "r")
file.read() # legge l'intero contenuto del file in una singola stringa
file.readline() # legge una riga alla volta
file.readlines() # legge tutte le righe e le restituisce come lista di righe
f.close() # non deve mai mancare

#? ESEMPIO READ
with open("./res/dati.txt", "r") as f:
   contenuto = f.read()
   print(contenuto)
   f.close()
with open("./res/dati.txt", "r") as f:
   prima_riga = f.readline()
   print("Prima riga: ", prima_riga)
   f.close()
with open("./res/dati.txt", "r") as f:
   righe = f.readlines()
   for riga in righe:
      print(riga.strip())
   f.close()
with open("./res/dati.txt", "r") as f:
   for riga in f:
      print(riga.strip())
   f.close()

#? ESEMPIO WRITE

with open("./res/dati.txt", "w") as f:
   f.write("Questo è un esempio di scrittura su file") # write() scrive una stringa nel file
   f.close()

linee = ["Prima riga\n", "Seconda riga\n", "Terza riga\n"]
with open("./res/dati.txt", "w") as f:
   f.writelines(linee) # writelines() scrive una lista di stringhe nel file

#? ESEMPIO ELSE E FINALLY

try:
   file = open("dati.txt", "r")
   contenuto = file.read()
except Exception as _:
   print("Errore: ", _)
else:
   dati = file.read()
   print("Dati letti: ", dati)
finally:
   if 'file' in locals():
      print("Chiusura del file")
      file.close()

#! CSV (Comma Separated Values)
import csv

# lettura da un file csv
with open("./res/dati.csv") as csvfile:
   lettore = csv.reader(csvfile, delimiter=",")
   for riga in lettore:
      print(riga)
   csvfile.close()

# scrittura su un file csv
dati = [
   ["Nome", "Età", "Città"],
   ["Samuele", 20, "Catania"],
   ["John", 23, "New York"]
]

with open("./res/output.csv", "w", newline="") as csvfile:
   scrittore = csv.writer(csvfile)
   scrittore.writerows(dati)
   csvfile.close()
   
#! JSON
import json

# lettura da un file json
with open("./res/config.json", "r") as file:
   dati = json.load(file)
   file.close()
print(dati)

# scrittura su un file json

infos = {
   "Nome" : "Samuele",
   "Età" : 20,
   "Città": "Catania"
}

with open("./res/output.json", "w") as file:
   json.dump(infos, file,  indent=4)
   file.close()