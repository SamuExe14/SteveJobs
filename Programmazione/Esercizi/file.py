import csv 

try:
  with open("file.csv", "a+") as my_file:
    my_file.seek(0)
    content = csv.reader(my_file)
    # writer = csv.writer(my_file)

  for riga in content:
    print(riga)
except Exception as _:
  print("Non è stato possibile aprire il file: ", _)
finally:
  my_file.close()