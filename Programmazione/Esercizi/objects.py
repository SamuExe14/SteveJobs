class Cerchio:
   def __init__(self, raggio):
      self.raggio = raggio

   @property
   def area(self):
      return 3.14 * (self.raggio * self.raggio)

cerchio = Cerchio(4)
print(cerchio.area)

from datetime import date
class Persona:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   
   @classmethod
   def fromBirthYear(cls, name, year):
      return cls(name, date.today().year - year)

   @staticmethod
   def isAdult(self):
      return self.age > 18

persona1 = Persona("Samuele", 20)
persona2 = Persona.fromBirthYear("John", 2000)
print(persona1.name, persona1.age)
print(persona2.isAdult(persona2))

class Archivio:
   class Documento:
      def __init__(self, nome, ID_documento):
         self.nome = nome
         self.ID_documento = ID_documento
      
   def __init__(self):
      self.documenti = []
   
   def aggiungi_documento(self, nome, ID_documento):
      nuovo_documento = Archivio.Documento(nome, ID_documento)
      self.documenti.append(nuovo_documento)
      
archivio = Archivio()
archivio.aggiungi_documento("12-04-25", 123123)
print(archivio.documenti[0].nome, archivio.documenti[0].ID_documento)