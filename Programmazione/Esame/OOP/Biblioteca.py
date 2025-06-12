# Crea una classe Biblioteca che gestisce una collezione di libri.
# Ogni libro è un oggetto della classe Libro con attributi come titolo, autore, anno, disponibile.
# Implementa:
# 
# Metodi per aggiungere, rimuovere, cercare libri.
# Un metodo per prestare e restituire un libro (cambia lo stato di disponibilità).
# Salvataggio e caricamento automatico della collezione su file (usa JSON o CSV).
# Gestione delle eccezioni per file mancanti o dati non validi.
# Usa proprietà per accedere/modificare lo stato di disponibilità.
# Implementa un decoratore per loggare ogni operazione.
import json

def menu():
   print(f"\n1) Aggiungere libro")
   print(f"2) Rimuovi libro")
   print(f"3) Cerca libro")
   print(f"4) Chiedi un prestito")
   print(f"5) Restituisci libro")

class Biblioteca:
   class Libro:
      def __init__(self, titolo, autore, anno, disponibile):
         self.titolo = titolo
         self.autore = autore
         self.anno = anno
         self.disponibile = disponibile
         
      def __repr__(self):
         return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Disponibile: {self.disponibile}"
      
   def __init__(self):
      self.biblioteca = []

   @property
   def get_biblioteca(self):
      try:
         with open("../res/biblioteca.json", "r") as file:
            biblioteca = json.load(file)
            print(biblioteca)
      except FileNotFoundError:
         print("Il file non esiste")
      except Exception as _:
         print(f"Errore generico: {_}")
      finally:
         if "file" in locals():
            file.close()
         
   def aggiungi_libro(self):
      titolo = input("\nInserire titolo del libro: ")
      autore = input("Inserire autore del libro: ")
      try:
         anno = int(input("Inserire anno di pubblicazione: "))
      except ValueError:
         print("È necessario inserire un anno di pubblicazione valido!")
         exit()
      except Exception as _:
         print(f"Errore: {_}")
         exit()
      try:
         disponibile = int(input("Inserire disponibilità (1/0): "))
         if disponibile != 1 and disponibile != 0:
            print("È necessario inserire un valore tra 0 e 1")
            exit()
      except ValueError:
         print("Inserire un valore tra 0 e 1")
         exit()
      
      self.get_biblioteca
      libro = self.Libro(titolo,autore,anno,disponibile)
      self.biblioteca.append(libro)
      print(self.biblioteca)
      try:
         with open("../res/biblioteca.json", "w") as file:
            json.dump([libro.__dict__ for libro in self.biblioteca], file, indent=4)
            print(self.biblioteca)
      except FileNotFoundError:
         print("Il file non esiste")
      except Exception as _:
         print(f"Errore generico: {_}")
      finally:
         if "file" in locals():
            file.close()
   def rimuovi_libro():
      pass
   
   def cerca_libro():
      pass
   
   def presta_libro():
      pass
   
   def restituisci_libro():
      pass

biblioteca = Biblioteca()

biblioteca.aggiungi_libro()