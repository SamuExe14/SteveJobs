import csv

def menu():
   print("1) Inserisci studente")
   print("2) Inserisci voto")
   print("3) Stampa singolo utente")
   print("4) Stampa tutti gli studenti")
   print("5) Esci")
   try:
      scelta = int(input("Scegli un'opzione (1-5): "))
      return scelta
   except ValueError:
      print("Valore non valido, inserire uno dei seguenti")
      exit()

class VotiStudenti:
   def __init__(self, matricola, nome, cognome, materia, voto):
      self.__matricola = matricola
      self.__nome = nome
      self.__cognome = cognome
      self.__voti = {
         materia : voto
      }
      
   def __str__ ( self ) :
      voti_str = "\n".join ([f"{m}: { v }" for m, v in self.__voti.items() ])
      return f"{self.__matricola} - {self.__nome } {self.__cognome }\n{voti_str}"
   
   def __repr__(self):
      return self.__str__()

   def aggiungi_voto(self):
      pass

Studenti = []

try:
   with open("./votistudenti.csv", "r", newline="") as file:
      reader = csv.reader(file)
      # next(reader)
      for riga in reader:
         # print(riga)
         matricola = riga[0]
         nome = riga[1]
         cognome = riga[2]
         materia = riga[3]
         voto = riga[-1]
         studente = VotiStudenti(matricola, nome, cognome, materia, voto)
         Studenti.append(studente)
except FileNotFoundError:
   print("Errore, file non trovato")

print(Studenti)
# while True:
#    scelta = menu()
#    match scelta:
#       case 1:
#          VotiStudenti.aggiungi_voto()
#          print(VotiStudenti)