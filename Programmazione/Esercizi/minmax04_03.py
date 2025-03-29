min = float("inf") # 
max = float("-inf")
sum = 0
counter = 0
pari = 0
dispari = 0

while True:
  num = int(input("Inserire un numero intero: "))
  if num == -1:
    break
  if num <= min:
    min = num
  if num >= max:
    max = num
  if num > max:
    max = num
  sum += num
  counter += 1
  if num % 2 == 0:
    pari += 1
  if num % 2 == 1:
    dispari += 1
print(f"dispari: {dispari}\n pari: {pari}\n massimo: {max}\n minimo: {min}")