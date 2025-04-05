
#* Scrivi un programma che calcola l'importo delle tasse da pagare in base al reddito annuale dell'utente
#* secondo la seguente tabella:
#* · Fino a 10000€ -> Nessuna tassa
#* · Tra 10001€ e 30000€ -> 10% sulla parte eccedente i 10000€
#* · Tra 30001€ e 60000€ -> 20% sulla parte eccedente i 30000€
#* · Oltre 60000€ -> 30% sulla parte eccedente i 60000€
#* Il programma deve calcolare l'importo totale delle tasse da pagare

reddito = float(input("Inserire reddito annuale: "))

if reddito >= 0 and reddito <= 10000:
  print("Nessuna tassa applicata")

elif reddito >= 10001 and reddito <= 30000:
  eccedente = reddito - 10000
  tasse = eccedente * 0.1
  print("Tasse da pagare in base al reddito:", tasse)

elif reddito >= 30001 and reddito <= 60000:
  eccedente = reddito - 30000
  tasse = eccedente * 0.2 + (10000 * 0.1)
  print("Tasse da pagare in base al reddito:", tasse)

elif reddito > 60000:
  eccedente = reddito - 60000 
  tasse = eccedente * 0.3 + (30000 * 0.2) + (10000 * 0.1)
  print(f"Tasse da pagare in base al reddito: {tasse:.2f}") 

else:
  print("Non è possibile inserire reddito in negativo")
  exit(1)