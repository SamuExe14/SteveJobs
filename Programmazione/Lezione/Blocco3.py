
#! Strutture decisionali

print("Hello world!") 
print("Hello", "world!")

nome = "Samuele"

print(f"Ciao {nome}")
print("Ciao", nome, sep=", ") # Ciao,Samuele
print("Ciao", nome, end="!\n") # Ciao Samuele! è necessario specificare il newline

multiline_string="""Questa stringa è stata costruita su più righe
e se non assegnata a nulla può essere considerata un commento multiriga"""
print(multiline_string)

raw_string=r"C:\Users\Samuele" # non tiene conto degli escape
print(raw_string)

# #! INPUT

# nome = input("Come ti chiami? ") # di default input() prende una stringa
# print(f"Ciao {nome}")

# età = int(input("Inserire l'età: ")) # è necessario specificare che input() deve prendere un int

# dati = input("Inserire nome ed età separati da spazi: ")
# nome, età = dati.split()
# print(f"Nome: {nome}, Età: {età}")

#! GESTIONE DELLE ECCEZIONI

try:
   numero = int(input("Inserire un numero: "))
   print("Numero inserito: ", numero)
except ValueError: #? ValueError: alza un'eccezione quando riceve un argomento che ha il tipo corretto ma con un valore non appropriato
   print("Errore: devi inserire un numero valido")
   
comando = input("Inserire un comando da eseguire: ")
# eval(comando) # ❌ potrebbe portare a falle di sicurezza in caso di injection di codice

for _ in range(3): # Max 3 tentativi
   valore = input("Inserisci un numero: ")
   if valore.isdigit():
      break
   print("Tentativi esauriti")

#! IMPORT IN PYTHON

import math
a = math.sqrt(16) # se si vuole usare una funzione di un modulo è necessario specificare il modulo stesso math.nome_funzione()

import datetime as dt # import con alias
dt.date(2025, 2, 12)

from datetime import timedelta # import di una singola funzione
d = timedelta(microseconds=-1) # se è stato fatto l'import della singola funzione non è necessario specificarne il modulo

import os         # interazioni con il sistema operativo
import sys        # variabili e funzioni di sistema
import json       # gestione dati in formato json
import re         # calcoli numerici e operazioni su array
import requests   # effettuare richieste HTTP

#! OPERATORI

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True

a = "Ciao"
c = a
print(a is c) # True

lista = [1, 2, 3]
print(2 in lista) # True
print(4 not in lista) # True

dati = {
   "Nome" : "Samuele",
   "Età"  : 20
}

for chiave, valore in dati.items(): # Return a new view of the dictionary’s items ((key, value) pairs)
   print(chiave, ":", valore)

numeri = [10, 20, 30, 40]
for i, num in enumerate(numeri): # enumerate() ritorna un oggetto enumerato che assegna un valore numerico al valore all'interno della lista
   print(f"Indice {i}: {num}")
   
#! FUNZIONI

def saluta(nome="Utente"): # è possibile assegnare un valore di default all'input 
   print(f"Ciao {nome}")
   
saluta() # Ciao Utente
saluta("Samuele") # Ciao Samuele

# def saluta(nome="Utente", cognome): # ❌ non è possibile specificare parametri con valori di default prima di altri senza predefiniti
def saluta(cognome, nome="Utente"): # ✅ 
   print(f"Ciao {nome} {cognome}")

def info(nome, età):
   print(f"{nome} ha {età} anni")

info("Samuele", 20) # sintassi posizionale
info(nome="Samuele", età=20) # ✅ sintassi nominale: aiuta a migliorare la leggibilità ed evita errori di ordine

def somma(*args): #? *args è un numero variabile di argomenti posizionali
   return sum(args)
print(somma(1,2,3,4,5))

def dettagli(**kwargs): #? **kwargs è un numero variabile di argomenti nominali
   print(kwargs)
dettagli(nome="Samuele", età=20)

quadrato = lambda x: x * x #* Le funzioni lambda sono funzioni anonime scritte in una sola riga
print(quadrato(4))

def fattoriale(n): # FUNZIONE RICORSIVA
   if n == 1:
      return 1
   return n * fattoriale(n - 1)

#! SCOPE DELLE VARIABILI

x = 10

def funzione():
   # global x #* se avessimo voluto usare la variabile globale avremmo dovuto specificarlo con il global
   x = 5
   print(x)

funzione() # x = 5 con scope locale
print(x) # x = 10 con scope globale

#! GENERATORI

def generatore():
   yield 1
   yield 2
   yield 3
   
print(list(generatore())) # [1, 2, 3]

gen = generatore()

print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
# print(next(gen)) ❌ se si chiama next() dopo l'ultimo valore viene lanciata l'eccezione StopIteration

for valore in generatore(): # è possibile ciclare all'interno di un generatore perché sono iterabili
   print(valore) 

gen = (x for x in range())
print(gen[5]) # ❌ Errore! I generatori non supportano l'indexing

print(list(gen)) # [1, 2, 3]
print(list(gen)) # [] Il generatore si esaurisce dopo un'iterazione, bisogna ricrearlo per riusarlo