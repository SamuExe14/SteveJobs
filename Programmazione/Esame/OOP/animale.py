# Creare una classe Animale che abbia gli attributi “nome” e “razza”. 
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni razza. 
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

class Animale:
   def __init__(self, nome, razza):
      self.nome = nome
      self.razza = razza

class Cane(Animale):
   def __init__(self, nome, razza):
      super().__init__(nome, razza)
   
   def emetti_suono(self):
      print(f"Sono {self.nome}, sono un {self.razza} e faccio Bau!")

class Gatto(Animale):
   def __init__(self, nome, razza):
      super().__init__(nome, razza)
   
   def emetti_suono(self):
      print(f"Sono un gatto e mi chiamo {self.nome}, sono di razza {self.razza} e faccio Miao!")
      
cane1 = Cane("Brian", "Beagle")
cane1.emetti_suono()
gatto1 = Gatto("Trottola", "Egiziana")
gatto1.emetti_suono()
