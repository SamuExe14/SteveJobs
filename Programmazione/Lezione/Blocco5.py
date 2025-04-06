
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
      file.close()

# print(locals())