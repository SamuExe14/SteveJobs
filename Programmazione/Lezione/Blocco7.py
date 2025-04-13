
#! CLASSI E OGGETTI

# Attributi: variabili associate alla classe o alla istanza
# Metodi: funzioni definite all'interno della classe che operano sugli attributi

class Persona:
   def __init__(self, nome, età):
      self.nome = nome
      self.età = età
   
   def saluta(self):
      return f"Ciao, sono {self.nome} e ho {self.età} anni"
   
# Creazione di un'istanza
p = Persona("Samuele", 20)
print(p.saluta())

class Esempio:
   valore = "Valore condiviso" # attributi di classe
   
   def __init__(self, valore):
      self.valore = valore

a = Esempio(10) # attributo di istanza
b = Esempio(20) # attributo di istanza

# -------------------------------------#

print(a.valore, b.valore)

class Rettangolo:
   def __init__(self, larghezza, altezza): # __init__ è il costruttore della classe. Permette di inizializzare attributi
      self.larghezza = larghezza
      self.altezza = altezza
   
   def area(self):
      return self.larghezza * self.altezza

rett = Rettangolo(10, 10)
print("Area del rettangolo:", rett.area())

#? METODI SPECIALI

class Persona:
   def __init__(self, nome, cognome):
      self.nome = nome
      self.cognome = cognome
   
   def __str__(self): # visualizzazione informale e leggibile
      return f"{self.nome}{self.cognome}"
   
   def __repr__(self): # rappresentazione ufficiale, utile nel debug
      return f"Persona('{self.nome}', '{self.cognome}')"
   
samuele = Persona("Samuele", "Leonardi")
print(str(samuele))
print(repr(samuele))

#? METODI DI CLASSE E METODI STATICI

from datetime import date

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   
   @classmethod # operano sulla classe anziché sull'istanza
   def fromBirthYear(cls, name, year):
      return cls(name, date.today().year - year)

   @staticmethod # non dipendono né dalla classe né dall'istanza
   def isAdult(age): 
      return age > 18

persona1 = Person("Samuele", 21)
persona2 = Person.fromBirthYear("Samuele", 2004)

print(persona2.age)
print(persona1.isAdult(22))

class Rettangolo:
   def __init__(self, larghezza, altezza):
      self._larghezza = larghezza
      self._altezza = altezza
   
   @property # per definire getter, setter e deleter
   def area(self):
      return self._larghezza * self._altezza

r = Rettangolo(5,3)
print("Area:", r.area)

#? INNER CLASSES
# Le classi interne possono essere definite all'interno di altre classi per raggruppare funzionalità correlate

class Biblioteca:
   class Libro:
      def __init__(self, titolo):
         self.titolo = titolo
   
   def __init__(self):
      self.libri = []
   
   def aggiungi_libro(self, titolo):
      nuovo_libro = Biblioteca.Libro(titolo)
      self.libri.append(nuovo_libro)

b = Biblioteca()
b.aggiungi_libro("La solitudine dei numeri primi")
print("Titolo del primo libro:", b.libri[0].titolo)

#? OVERLOADING DEGLI OPERATORI

class Vettore:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   
   def __add__(self, other):
      return Vettore(self.x + other.x, self.y + other.y)
   
   def __str__(self):
      return f"Vettore({self.x}, {self.y})"

v1 = Vettore(1,2)
v2 = Vettore(3,4)
print(v1 + v2)

#? CREAZIONE DI CLASSI IMMUTABILI

from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
print(p)

from dataclasses import dataclass

@dataclass(frozen=True) # permette di creare un oggetto immutabile
class PersonaImmutabile:
   nome: str
   età: int
   
persona = PersonaImmutabile("Samuele", 21)
print(persona)

#? GESTIONE DEGLI ERRORI

class Calcolatrice:
   def dividi(self, a, b):
      try:
         return a / b
      except ZeroDivisionError:
         print("Errore: divisione per 0!")

calc = Calcolatrice()
print(calc.dividi(6,2))

#? MODULI 
from res.module import Prodotto

p = Prodotto("Penna", 1.5)
print(p.mostra())

print("#################################")
#? INCAPSULAMENTO

class Contatore:
   def __init__(self):
      self._conteggio = 0
   
   def incrementa(self):
      self._conteggio += 1
   
   def get_conteggio(self):
      return self._conteggio

c = Contatore()
# c.incrementa()
print(c.get_conteggio())

#? ASTRAZIONE

from abc import ABC, abstractmethod

class Forma(ABC):
   @abstractmethod
   def area(self, lato):
      pass
   
class Quadrato(Forma):
   def __init__(self, lato):
      self.lato = lato

   def area(self):
      return self.lato * self.lato

# f = Forma() # ❌ non si possono istanziare classi astratte
q = Quadrato(4)
print(q.area())

#? EREDITARIETÀ

class Animale:
   def parla(self):
      return "Suono generico"

class Cane(Animale):
   def parla(self):
      return "Bau!"

animale = Animale()
cane = Cane()

print("Animale fa:", animale.parla())
print("Cane fa:", cane.parla())

#? EREDITARIETÀ MULTIPLA

class Madre:
   def saluta(self):
      return "Ciao dalla madre"

class Padre:
   def saluta(self):
      return "Ciao dal padre"
   
class Figlio(Madre, Padre):
   pass

figlio = Figlio()
print(figlio.saluta()) # prende il metodo della classe Madre per l'ordine della risoluzione dei metodi

#? POLIMORFISMO

class Forma:
   def area(self):
      pass

class Quadrato(Forma):
   def __init__(self, lato):
      self.lato = lato
   
   def area(self):
      return self.lato * self.lato

class Cerchio(Forma):
   def __init__(self, raggio):
      self.raggio = raggio
   
   def area(self):
      return 3.14 * (self.raggio * self.raggio)
   
forme = [Quadrato(3), Cerchio(7)]

for f in forme:
   print(f.area())
   
#? COMPOSIZIONE

class Motore:
   def accendi(self):
      return "Motore acceso"
   
class Macchina:
   def __init__(self):
      self.motore = Motore()
   
   def avvia(self):
      return self.motore.accendi()

veicolo = Macchina()
print(veicolo.avvia())

#? DISTRUTTORE

class Esempio:
   def __del__(self):
      print("L'oggetto è stato distrutto")
   
e = Esempio()
del e # distruttore della classe Esempio

#? OVERRIDING E OVERLOADING

from multipledispatch import dispatch

class Overload:
   @dispatch(int,int)
   def add(self, a, b):
      x = a + b
      return x

   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a + b + c
      return x

esempio = Overload()
print(esempio.add(1,2))
print(esempio.add(1,2,3))

#? CREAZIONE DINAMICA DI UNA CLASSE

def saluta(self):
   return "Ciao dal dinamico"

Dinamica = type("Dinamica", (object,), {"saluta": saluta})
d = Dinamica()
print(d.saluta())

#? DECORATORE PERSONALIZZATO PER LOGGING

def logger(func):
   def wrapper(*args, **kwargs):
      print(f"Esecuzione di {func.__name__}")
      return func(*args, **kwargs)
   return wrapper

class Matematica:
   @logger
   def somma(self, a, b):
      return a + b

m = Matematica()
print(m.somma(3,4))

##############################################

class Rettangolo:
   def __init__(self, larghezza, altezza):
      self.larghezza = larghezza
      self.altezza = altezza
   
   @property
   def area(self):
      return self.larghezza * self.altezza

rett = Rettangolo(4, 5)
print(rett.area)