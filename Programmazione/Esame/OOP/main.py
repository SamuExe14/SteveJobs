class Samuele: # classe con attributi standard
   nome = "Samuele" 
   cognome = "Leonardi"

class Persona:
   def __init__(self, nome, cognome):
      self.nome = nome
      self.cognome = cognome

   def __str__(self): #  visualizzazione informale e leggibile
      return f"{self.nome}{self.cognome}"
   
   def __repr__(self): # rappresentazione ufficiale, utile nel debug
      return f"Persona('{self.nome}', '{self.cognome}')"

   def saluta(self):
      print(f"Ciao sono {self.nome} {self.cognome}")
      
class Insegnante(Persona):
   def __init__(self, nome, cognome):
      super().__init__(nome, cognome) # con super() si intende che eredita automaticamente dalla sua classe padre
   
samuele1 = Samuele()
samuele2 = Samuele()

persona1 = Persona("Samuele", "Leonardi")
persona1.saluta()

print(str(persona1))
print(repr(persona1))