
#! Inserimento multiplo
dati = input("Inserire nome ed età separati da spazi: ")
nome, eta = dati.split()
print(f"Nome: {nome}, Età: {eta}, {dati}")

x = int(eta) >= 18 # viene messo il valore booleano
print(x) # True o False

#---------------------------------#
#! Selezione
x = 5
y = 10

if x > 0 and y < 20:
  print("Entrambi i numeri sono validi")

#! Cicli
for i in range(5):
	print(i) # stampa 1 2 3 4 5

#? Su una lista
frutta = ["mela", "banana", "ciliegia"]
for elemento in frutta:
	print(elemento)

#? Su un dizionario
dati = {"nome": "Alice", "eta": 20}
# ----------------------------------------------#

reddito = float(input("Inserire reddito annuale: "))
if reddito > 60000:
  eccedente = reddito - 60000 
  tasse = eccedente * 0.3 + (30000 * 0.2) + (10000 * 0.1)
  print("Tasse da pagare in base al reddito: {tasse:.2f}")  # è possibile specificare 
																														#  la precisione con il seguente formato

min = float("-inf") # va a mettere -infinito all'interno della variabile
max = float("inf") # va a mettere +infinito all'interno della variabile