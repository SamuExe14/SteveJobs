# # Crea un programma che gestisca un magazzino di prodotti.

# Ogni prodotto è rappresentato da un dizionario con chiavi: nome, categoria, prezzo, quantità.
# Salva tutti i prodotti in una lista.
# Permetti all’utente di:
# Aggiungere un nuovo prodotto (controlla che il nome non sia già presente).
# Modificare la quantità o il prezzo di un prodotto esistente.
# Rimuovere un prodotto.
# Visualizzare tutti i prodotti di una certa categoria (usa filter).
# Calcolare il valore totale del magazzino.
# Gestisci input non validi e casi particolari (es. quantità negativa).

def menu():
      print("\nMenu:")
      print("1. Aggiungi prodotto")
      print("2. Modifica prodotto")
      print("3. Rimuovi prodotto")
      print("4. Visualizza prodotti per categoria")
      print("5. Calcola valore totale del magazzino")
      print("6. Esci")
      try:
         scelta = int(input("Scegli un'opzione (1-6): "))
         return scelta
      except ValueError:
         print("Errore: inserisci un numero valido.")
         return 0

def aggiungi_prodotto(magazzino):
   try:
      nome = input("Inserisci il nome del prodotto: ")
      for prodotto in magazzino:
         if prodotto["nome"].lower() == nome.lower():
            print("Errore: il prodotto esiste già.")
   except ValueError:
      print("Errore: nome non valido.")
      return 1
   try:
      categoria = input("Inserisci la categoria del prodotto: ")
   except Exception as _:
      print("Errore: categoria non valida.")
      return 1
   try:
      prezzo = float(input("Inserisci il prezzo del prodotto: "))
   except ValueError:
      print("Errore: prezzo non valido.")
      return 1
   try:
      quantita = int(input("Inserisci la quantità del prodotto: "))
      if quantita < 0:
         raise ValueError("La quantità non può essere negativa.")
   except ValueError:
      print("Errore: quantità non valida.")
      return 1
   magazzino.append({
      "nome": nome,
      "categoria": categoria,
      "prezzo": prezzo,
      "quantita": quantita
   })
   print(f"Prodotto '{nome}' aggiunto con successo.")
   
def modifica_prodotto(magazzino):
   nome = input("Inserisci il nome del prodotto da modificare: ")
   for prodotto in magazzino:
      if prodotto["nome"].lower() == nome.lower():
         try:
            prezzo = float(input(f"Inserire il nuovo prezzo di {nome}: "))
            if prezzo < 0:
               raise ValueError ("Il prezzo non può essere negativo")
            prodotto["prezzo"] = prezzo
         except ValueError:
            print("Errore! Inserire un prezzo valido")
         try:
            quantita = int(input(f"Inserire la nuova quantità di {nome}: "))
            if quantita < 0:
               raise ValueError("Non è possibile inserire una quantità negativa")
            prodotto["quantita"] = quantita
         except ValueError:
            print("Errore: quantità non valida")
      else:
         print(f"Il prodotto di nome {nome} non è stato trovato in magazzino")
         break
   try:
      print(prodotto)
   except UnboundLocalError:
      print(f"{nome} non è stato trovato in magazzino")

def get_magazzino(magazzino):
   for prodotto in magazzino:
      for key, value in prodotto.items():
         print(f"{key}:{value}")

def rimuovi_prodotto(magazzino):
   nome = input("Inserire prodotto che si vuole rimuovere dal magazzino: ")
   for prodotto in magazzino:
      if prodotto["nome"].lower() == nome.lower():
         print(f"{nome} trovato, eliminazione in corso")
         del prodotto["nome"]
         del prodotto["categoria"]
         del prodotto["prezzo"]
         del prodotto["quantita"]
      break
   try:
      print(prodotto)
   except UnboundLocalError:
      print(f"{nome} non è stato trovato in magazzino")
   
def get_tot_magazzino(magazzino):
   totale = 0
   for prodotto in magazzino:
      totale += prodotto["prezzo"]
   print(f"Il totale del magazzino è {float(totale)}")

magazzino = []

while True:
   scelta = menu()   
   match scelta:
      case 1:
         aggiungi_prodotto(magazzino)
         get_magazzino(magazzino)
         # print(magazzino)
      case 2:
         modifica_prodotto(magazzino)
         get_magazzino()
         # print(magazzino)
      case 3:
         rimuovi_prodotto(magazzino)
         get_magazzino(magazzino)
      case 4:
         # TODO mi rompo il cazzo a fare sta parte
         print("")
      case 5:
         get_tot_magazzino(magazzino)
      case 6:
         break