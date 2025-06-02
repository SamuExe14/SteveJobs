# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, 
# ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:
   def __init__(self, nome, eta, sesso):
      self.nome = nome
      self.eta = eta
      self._sesso = sesso
   
   @property
   def presenta(self):
      print(f"Ciao sono {self.nome} e ho {self.eta} anni {self._sesso}")
   
marco = Persona("Marco", 21, "M")
marco.presenta
