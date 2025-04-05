
#! LISTE

lista = [1, 2, 3, "quattro", 5.0]
print(lista)

new_list = [10, 20, 30, 40, 50]
# Indicizzazione negativa
print(new_list[-1]) # 50
print(new_list[-2]) # 40
# Slicing 
print(new_list[:3]) # 10, 20, 30

#? OPERAZIONI SULLE LISTE

numeri = [10, 20, 30, 40]

sotto_lista = numeri[1:3] # crea una sottolista facendo uno slicing
numeri.remove(20) # cerca all'interno della lista e rimuove se lo trova
numeri.pop() # estrae e ritorna l'ultimo elemento
numeri.pop(1) # se passato un indice pop() estrae l'elemento in quella posizione
numeri.append(50) # non esiste il metodo push() 
numeri += [6, 2, "Ciao"] # effettua un inserimento multiplo nella lista
print(numeri)

#? OPERAZIONI AVANZATE SULLE LISTE

my_list = [10, 20, 30, 40, 50, 60]

my_list.insert(2,25) # inserisce 25 alla posizione 2
print("Lista completa iniziale: ",my_list)
slicing_step = my_list[::2] # effettua uno sling a due a due
print("Lista con slicing a due a due: ",slicing_step)

my_list.reverse() # inverte la lista
print("Lista invertita: ", my_list)

del my_list[1:4] # elimina gli elementi dalla posizione 1 alla posizione 4

indice = my_list.index(60) # trova l'indice che corrisponde all'elemento 50
print("Indice dell'elemento 60:",my_list.index(60))
print(my_list)

#? ALTRE OPERAZIONI SULLE LISTE

from functools import reduce

lista = [50, 55, 60, 70, 40, 90]
print(lista)

def my_filter(score):
   return score >= 60

lista = list(filter(my_filter, lista)) # crea una nuova lista con gli elementi che sono stati filtrati
print(lista)

pets_list = ['giacomo', 'filippo', 'giuseppe', 'john doe']
uppered_pets = list(map(str.upper, pets_list)) # 
print(uppered_pets)

#! TUPLE

#* A differenza delle liste, le tuple sono immutabili

tuple = (10, 20, "Valore", "Elemento")
print(tuple)
del tuple # per eliminare l'intera tupla

#? OPERAZIONI SULLE TUPLE
# Nonostante sia impossibile modificare gli elementi della tupla è possibile accedervi, effettuare lo slicing e la concatenazione
coordinate = (10, 20)
print(coordinate)

coordinate_cat = coordinate + (30, 40)
del coordinate

#! DIZIONARI

studente = {"nome": "Samuele", "età": 20, "corso": 35 }
print(studente)

#? OPERAZIONI SUI DIZIONARI

print(studente["nome"]) # accesso a un valore
studente["età"] = 21 # modifica di un valore
del studente["corso"] # rimozione di un campo

for chiave, valore in studente.items(): # iterazione su chiavi e valori 
   print(chiave, ":", valore)
   
studente["città"] = "Catania" # aggiunta di un valore all'interno del dizionario

#! STRINGHE

#? OPERAZIONI SULLE STRINGHE
stringa = "Ciao"
stringa2 = "Mondo"

stringa_cat = stringa + " " + stringa2 # concatenazione
print(stringa2[:3]) # slicing

testo = "   Python è molto bello    "
print("Maiuscolo:", testo.upper())
print("Minuscolo:", testo.lower())
print("Diviso:", testo.split())
print(testo.lstrip()) # rimuove gli spazi da sinistra
print(testo.rstrip()) # rimuove gli spazi da destra
print(testo.strip()) # rimuove gli spazi da entrambi i lati

#! SET

#* I set sono collezioni non ordinate di elementi UNICI utili per operazioni insiemistiche

numbers = {1, 2, 3, 3, 4, 5, 6} # non verrà mostrato due volte il 3 perché i duplicati vengono eliminati
print(numbers)

#? OPERAZIONI SUI SET
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2) # unione
print(set1 & set2) # intersezione
print(set1 - set2) # differenza

c = [1, 2, 3, 4, 5, 6]
c = set(c) # trasforma la lista in un set

print(c)