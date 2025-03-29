# import mio_modulo
import libs.settings as mine # è un alias
print(mine.saluta("Samuele"))

from libs.settings import saluta 
from libs.settings import moltiplica

saluta("Samuele")
print(moltiplica(5,6))

#! GESTIONE DELLE ECCEZIONI

a = input("Inserisci un numero: ")

try:
	b = int(a)
except Exception as e: # se non si usa e si usa _
	print("Si è verificato un errore", e)

try:
  file = open("esempio.txt", "r")
  file.write("Log iniziale")
except Exception as _:
  print("Errore: ", _)
finally: # che venga eseguito il try o l'except esegue le istruzioni sotto il finally
  try:
    file.close()
  except Exception as _:
    print("Non funziona un cazzo:", _)

with open("file.txt", "r") as f:
  contenuto = f.read()
  print(contenuto)
with open("file.txt", "r") as f:
  prima_riga = f.readline()
  print("Prima riga ", prima_riga)
  
#! FILE CSV

import csv

with open("dati.csv", "r") as csvfile:
  lettore = csv.reader(csvfile, delimiter=", "), 
  for riga in lettore:
    print(riga)