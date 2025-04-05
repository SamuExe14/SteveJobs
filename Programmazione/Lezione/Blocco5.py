
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