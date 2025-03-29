def somma(x,y):
  sum = x + y
  print(f"La somma è {sum}")
  
def quadrato(x):
  quadrato = x * x
  print(f"Il quadrato è { quadrato }")
    
def area(base,altezza):
  area = (base * altezza) / 2
  print(f"L'area del triangolo è {area}")

def pariDispari(num):
  if(num % 2 == 0):
    print("True")
  else:
    print("False")

def vocali(parola):
  for car in parola:
    if(car == 'a' or car == 'e' or car == 'i' or car == 'u' or car == 'u'):
      print(car)

def è_primo(numero):
  # Controlla se il numero è minore o uguale a 1
  if numero <= 1:
      return False
  # Controlla se il numero è 2 o 3
  if numero <= 3:
      return True
  # Escludi i numeri pari e i multipli di 3
  if numero % 2 == 0 or numero % 3 == 0:
      return False
  # Verifica i divisori da 5 in poi
  i = 5
  while i * i <= numero:
      if numero % i == 0 or numero % (i + 2) == 0:
          return False
      i += 6
  return True

def generatore():
  for i in range(0,1000):
    if è_primo(i):
      print(i)

# x = int(input("Inserire due numeri per la somma "))
# y = int(input())
# somma(x,y)

# z = int(input("Inserire un numero per averne il quadrato "))
# quadrato(z)

# base = int(input("Inserire base e altezza "))
# altezza = int(input())
# area(base,altezza)

# num = input("Inserire un numero pari per True, dispari per False ")

# parola = input("Inserire una parola per contarne le vocali ")
# vocali(parola)

primo = int(input("Inserire un numero "))

if è_primo(primo):
  print(f"{primo} è primo")
else:
  print(f"{primo} non è primo")

generatore()  