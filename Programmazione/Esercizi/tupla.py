tupla = (10,22,34,213,4,87)

print(tupla[0:4])

nuova_tupla = (0, 7, 8, 45, 89)

tupla = tupla + nuova_tupla

print(tupla)
tupla = (tuple(sorted(tupla)))

print(tupla)