# Crea un programma che gestisca una rubrica di contatti.
# 
# Ogni contatto ha nome, telefono, email.
# Permetti di aggiungere, modificare, eliminare e cercare contatti.
# Salva e carica i dati da un file CSV.
# Gestisci eventuali errori di input e di file (es. file non trovato, dati non validi).
import csv

def menu():
   print("\nMenu")
   print("1) Nuovo contatto")
   print("2) Modifica contatto")
   print("3) Elimina contatto")
   print("4) Cerca contatto")
   print("5) Termina programma")
   try:
      scelta = int(input())
      return scelta
   except ValueError:
      print("Inserire un valore valido")

def get_rubrica(path, rubrica):
   with open(f"{path}", "r") as file:
      reader = csv.reader(file, delimiter=",")
      for raw in reader:
         rubrica.append(raw)
         # print(rubrica)


def aggiungi_contatto(path, rubrica):
   try:
      with open(f"{path}", "w", newline="") as csvfile:
         nome = input("Inserire nome contatto: ")
         try:
            telefono = int(input("Inserire numero di telefono: "))
            email = input("Inserire email: ")
            rubrica.append([nome,telefono,email])
            writer = csv.writer(csvfile)
            writer.writerows(rubrica)
         except ValueError:
            print("Inserire un numero di telefono valido")
   except FileNotFoundError:
      print("File non trovato")
   finally:
      if 'csvfile' in locals():
         csvfile.close()
         
# FIXME stu cazzi cosu nun funziona

def modifica_contatto(path,rubrica):
   nome = input("Inserire nome contatto da modificare: ")
   for contatto in rubrica:
      print(contatto[0])
      if contatto[0].lower() == nome.lower():
         nome_nuovo = input("Inserire nuovo nome del contatto: ")
         try:
            telefono_nuovo = int(input("Inserire nuovo telefono del contatto: "))
         except ValueError:
            print("Numero di telefono non valido")
         email_nuova = input("Inserire nuova email del contatto: ")
         contatto[0] = nome_nuovo
         contatto[1] = telefono_nuovo
         contatto[-1] = email_nuova
         try:
            with open(f"{path}", "w", newline="") as csvfile:
               writer = csv.writer(csvfile)
               writer.writerows(rubrica)
         except FileNotFoundError:
            print("File non trovato")
   print("Contatto non presente in rubrica")

rubrica = []
# rubrica.append(["Nome", "Età", "Email"])
# rubrica.append()

get_rubrica("./res/rubrica.csv", rubrica)
# print(rubrica)

while True:
   scelta = menu()
   match scelta:
      case 1:
         aggiungi_contatto("./res/rubrica.csv",rubrica)
      case 2:
         modifica_contatto("./res/rubrica.csv",rubrica)
      case 3:
         elimina_contatto(rubrica) # TODO completare
      case 4:
         cerca_contatto(rubrica) # TODO completare p.2
      case 5:
         break