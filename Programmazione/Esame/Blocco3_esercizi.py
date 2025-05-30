# Scrivi un programma che chiede all’utente di inserire due numeri e stampa la loro somma. 
# Gestisci il caso in cui l’utente inserisca valori non numerici.
try:
   val = int(input("Inserire il primo numero intero: "))
   val1 = int(input("Inserire il secondo numero intero: "))
   print("La somma è:", val + val1)
except ValueError:
   print("Errore: inserire un numero intero valido.")
   
# Crea una lista di numeri da 1 a 10. Stampa solo i numeri pari usando un ciclo for e l’operatore in.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numeri pari nella lista:")
for i in lista:
   if i % 2 == 0:
      print(f"{i}")

# Crea un dizionario con i nomi di tre amici e le loro età. Stampa ogni coppia chiave-valore con un ciclo for.
dict = {
   "Nomi" : [
      "Samuele",
      "Simone",
      "Mirko"
   ],
   "Età" : [
      21,
      16,
      48
   ]
}

for nome, eta in zip(dict["Nomi"], dict["Età"]):
   print(f"{nome} ha {eta} anni")
   
# Chiedi all’utente di inserire un numero e verifica se è presente nella lista 
# [1, 2, 3, 4, 5]. Stampa un messaggio appropriato.

lista_numeri = [1, 2, 3, 4, 5]
try:
   numero_utente = int(input("Inserisci un numero tra 1 e 5: "))
   if numero_utente in lista_numeri:
      print(f"Il numero {numero_utente} è presente nella lista.")
   else:
      print(f"Il numero {numero_utente} non è presente nella lista.")
except ValueError:
   print("Errore: inserire un numero valido.")

# Scrivi una funzione saluta che prende un nome come parametro (con valore di default "Utente") 
# e stampa "Ciao <nome>". Chiama la funzione almeno due volte, una senza parametri e una con un nome.

def saluta(utente="utente"):
   print(f"Ciao {utente}")
   
saluta()
saluta("Samuele")

# Chiedi all'utente di inserire due numeri interi.
# Gestisci eventuali ValueError se l'input non è numerico.
# Se i numeri sono validi, stampa la loro divisione.
# Gestisci l'eccezione ZeroDivisionError se il secondo numero è 0.
# Usa un ciclo for con massimo 3 tentativi per l'inserimento corretto.

try:
   num = int(input("Inserire un numero intero: "))
   num1 = int(input("Inserire un altro numero intero: "))
   print(f"La divisione di {num}/{num1}={num/num1}")
except ValueError:
   print("Inserire un valore intero valido")
except ZeroDivisionError:
   print("Non è possibile effettuare una divisione per zero")
   
def calcola_media(*args):
   if len(args) == 0:
      return ValueError
   return sum(args) / len(args)

def info_utente(**kwargs):
   for key,value in kwargs.items():
      print(f"{key} = {value}")

def n_potenze(num):
   # if num == 0:
   #    return 1
   for x in range(num):
      print(x)
   # return y
      
print(calcola_media(10,6,8))
info_utente(Nome="Samuele", Età=21)

