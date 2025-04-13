class Prodotto:
   def __init__(self, nome, prezzo):
      self.nome = nome
      self.prezzo = prezzo
   
   def mostra(self):
      return f"{self.nome}: {self.prezzo}"
