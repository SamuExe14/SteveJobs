def cambiaNome(nome, nuovo_nome):
  nome = nuovo_nome

def saluta(nome):
  print(f"Ciao {nome}")
  
def saluta(cognome, nome="Utente"):
  print(f"Ciao {nome} {cognome}")


nome = "Anna"
saluta("Sgroi", "Alfio") #! sintassi posizionale
saluta(cognome="Sgroi", nome="Alfio") #! sintassi nominale
# cambiaNome(nome, "Alfio")
# print(f"Nuovo nome: {nome}")

# ----------------------------------------------------------------#
#? SCOPE

x = 10

def funzione():
  x = 5
  print(x)
  
funzione()
print(x)

