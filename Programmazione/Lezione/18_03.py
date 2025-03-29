
#! LISTE
lista = [10,20,30,40,50]

print(lista[-1]) # 50
print(lista[-3]) # 30

print(lista[-4:-1]) # [20, 30, 40]

print(lista[:3]) # stampa i primi tre elementi
print(lista[3:]) # stampa gli elementi dopo il terzo indice

from functools import reduce

mia_lista = [50, 55, 60, 70, 30, 90]

def my_filter(score):
  return score >= 60

promossi = list(filter(my_filter, mia_lista))
promossi_lambda = list(filter(lambda promossi: promossi >= 60, mia_lista))
print(promossi)

#! TUPLE
coordinate = (10, 20) # vengono definite con ()
print("Coordinate: ", coordinate)

nuova_tupla = coordinate + (30,40) # possono essere concatenate con il '+'
print("Tuple concatenate: ", nuova_tupla)

# nuova_tupla.append(10) # ❌ NON È POSSIBILE EFFETTUARE QUESTO TIPO DI OPERAZIONI
del coordinate # ✅ si può solo eliminare l'intera tupla

#! DIZIONARI

info = {
  "nome":"Bob", 
  "età": 25
}
info["città"] = "Milano" # aggiunge un elemento al dizionario
print("Info studente:", info)

for key, value in info.items():
  print(f"{key=}", f"{value=}")

for key in info:
  print(f"{key} = {info[key]}")

# for value in info.values():
  # print
  
#! STRINGHE

testo = "python è fantastico"
print("Maiuscolo", testo.upper())
print("Diviso:", testo.split())

name = '  Captain America  '
name.lstrip() # rimuove gli spazi a sinistra
name.rstrip() # rimuove gli spazi a destra
name.strip() # rimuove gli spazi da entrambi i lati
print(name)

#! SET
a = {1,2,3,4}
b = {3,4,5,6}
c = [1,2,3,4,5,6]

print("Unione: ", a | b)
print("Intersezione: ", a & b)
print("Differenza: ", a - b)
print("Set a partire da una lista: ", set(c))
