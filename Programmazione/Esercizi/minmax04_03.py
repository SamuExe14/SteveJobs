
#* Scrivi un programma che permette all'utente di inserire una sequenza di numeri fino a quando inserisce -1
#* Alla fine il programma deve:
#* · Stampare il numero massimo e minimo inserito 
#* · Calcolare la media dei numeri
#* · Contare quanti numeri pari e dispari sono stati inseriti
min = float("inf")
max = float("-inf")
sum = 0
counter = 0
pari = 0
dispari = 0

while True:
  num = int(input("Inserire un numero intero: "))
  if num == -1:
    break
  if num <= min:
    min = num
  if num >= max:
    max = num
  if num > max:
    max = num
  sum += num
  counter += 1
  if num % 2 == 0:
    pari += 1
  if num % 2 == 1:
    dispari += 1
print(f"\ndispari: {dispari}\npari: {pari}\nmassimo: {max}\nminimo: {min}")