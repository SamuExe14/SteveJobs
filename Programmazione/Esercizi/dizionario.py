# libro = {
#   "Titolo" : "La solitudine dei numeri primi",
#   "Autore" : "Paolo Giordano",
#   "Anno" : 2008
# }

# libro["Pagine"] = 246

# print(libro)

from collections import OrderedDict

lista_libri = [
  {
    "Titolo" : "La solitudine dei numeri primi",
    "Anno" : 2008,
    "Autore" : "Paolo Giordano",
    "ISBN" : 9780143177449
  },
  {
    "Titolo" : "Il significato dei sogni",
    "Anno" : 1899,
    "Autore" : "Sigmund Freud",
    "ISBN" : 9780192100498
  }
]

# print(lista_libri)


print(OrderedDict(lista_libri))