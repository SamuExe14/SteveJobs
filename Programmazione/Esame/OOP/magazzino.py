# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
#
# La classe dovrà avere i seguenti metodi:
#
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
#
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

def menu():
   print("1) Aggiungi prodotto")
   print("2) Rimuovi prodotto")
   print("3) Calcola costi magazzinaggio")
   print("4) Mostra magazzino")
   print("5) Esci") 
   try:
      scelta = int(input("Scegliere tra le seguenti opzioni: "))
   except ValueError:
      print("Errore, inserire un valore corretto tra quelli citati")
   return scelta

class GestoreMagazzino:
   class Prodotto:
      def __init__(self, nome, prezzo, scorta):
         self.prodotto = {
            "Nome" : nome,
            "Prezzo" : prezzo,
            "Scorta" : scorta
         }
      
      def __repr__(self):
         return f"{self.prodotto}"
         
   def __init__(self, costo_magazzinaggio):
      self.magazzino = []
      self.costo_magazzinaggio = costo_magazzinaggio

   @property
   def calcola_costi_magazzinaggio(self):
      totale_costo_magazzinaggio = 0
      for prodotto in self.magazzino:
         totale_costo_magazzinaggio += self.costo_magazzinaggio
      print(f"Il totale dei costi di magazzinaggio ammontano a {totale_costo_magazzinaggio}")

   @property
   def mostra_magazzino(self):
      print(self.magazzino)

   def aggiungi_prodotto(self, nome, prezzo, scorta):
      nuovo_prodotto = GestoreMagazzino.Prodotto(nome, prezzo, scorta)
      self.magazzino.append(nuovo_prodotto)
      print(f"È stato aggiunto {nome} al magazzino\n")
   
   def elimina_prodotto(self):
      try:
         nome_prodotto = input("\nInserire nome del prodotto da rimuovere: ")
      except Exception as _:
         print(f"Errore generico: {_}")
      for prodotto in self.magazzino:
         if nome_prodotto.lower() == prodotto.prodotto["Nome"].lower():
            print(f"{nome_prodotto} è stato trovato, eliminazione in corso")
            self.magazzino.remove(prodotto)
         else:
            print("Prodotto non trovato all'interno del magazzino")

try:
   costo_magazzinaggio = float(input("Inserire costo del magazzinaggio: "))
except ValueError:
   print("Errore, inserire un valore valido; Uscita in corso")
magazzino = GestoreMagazzino(costo_magazzinaggio)

while True:
   scelta = menu()
   match scelta:
      case 1:
         try:
            nome = input("Inserire nome del prodotto: ")
         except Exception as _:
            print(f"Errore: {_}")
         try:
            prezzo = float(input("Inserire prezzo del prodotto: "))
         except ValueError:
            print("Errore, inserire un valore valido")
         except Exception as _:
            print(f"Errore: {_}")
         try:
            scorta = input("Inserire tipo di scorta: ")
         except Exception as _:
            print(f"Errore: {_}")
         magazzino.aggiungi_prodotto(nome,prezzo,scorta)
      case 2:
         magazzino.elimina_prodotto()
      case 3:
         magazzino.calcola_costi_magazzinaggio
      case 4:
         magazzino.mostra_magazzino
      case 5:
         print("Terminazione programma in corso, eliminazione degli oggetti fin'ora creati")
         break

if "magazzino" in locals():
   print("magazzino trovato")
   del magazzino