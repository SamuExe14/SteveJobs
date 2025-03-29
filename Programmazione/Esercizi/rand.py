import random

num = random.randint(1, 100)

utente = int(input("Prova ad indovinare il numero: "))

while utente != num:
  utente = int(input("Prova ad indovinare il numero: "))
  if utente < num:
    print("Troppo basso")
  elif utente > num:
    print("Troppo alto")

print("Numero trovato!")