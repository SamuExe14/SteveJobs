# Crea una classe Cerchio con attributo raggio e un metodo per calcolare l'area
class Cerchio:
   def __init__(self, raggio):
      self.raggio = raggio

   @property
   def area(self):
      return (self.raggio * self.raggio) * 3.14

cerchio = Cerchio(20)
cerchio.area

# Implementa una classe Archivio con una inner 
# class Documento e un metodo per aggiungere documenti

class Archivio:
   class Documento:
      def __init__(self, numero_documento):
         self.numero_documento = numero_documento
      
      def __repr__ (self):
         return f"Documento(numero={self.numero_documento})"

   def __init__(self):
      self.dossier = []

   def aggiungi_documento(self, numero_documento):
      nuovo_documento = Archivio.Documento(numero_documento)
      self.dossier.append(nuovo_documento)

   # @property
   def mostra_archivio(self):
      print (self.dossier)

archivio = Archivio()
archivio.aggiungi_documento(123456)
archivio.aggiungi_documento(123123131)
archivio.mostra_archivio()

del archivio