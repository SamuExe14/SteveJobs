print("Inserire due numeri interi")

# if x > 0:
#   print("Il numero  positivo")
# elif x < 0:
#   print("Il numero  negativo")
# else: 
#   print("Il numero  zero")

x = int(input())
y = int(input())

somma = x + y
diff = x - y
prod = x * y
quoz = float(x) / y
quoz_int = x // y
modulo = x % y

print("La somma di", x, "e", y, "è", somma)
print("La differenza di", x, "e", y, "è", diff)
print("Il prodotto di", x, "e", y, "è", prod)
print("Il quoziente di", x, "e", y, "è", quoz)
print("La divisione intera di", x, "e", y, "è", quoz_int)
print("Il modulo di", x, "e", y, "è", modulo)

#! ciclo for per sommare i numeri da 1 a 10
#* ciclo while per contare quante iterazioni sono necessarie per superare una somma di 100
sum = 0
for iter in range(1,11):
  sum += iter
  print (sum)