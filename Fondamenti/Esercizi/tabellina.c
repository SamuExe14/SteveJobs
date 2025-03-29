// Scrivi un programma che, dato in input un numero, ne stampa la tabellina
//
// Scrivi un programma che, data in input un numero, se tale numero è minore o uguale di 15 ne stampa la tabellina,
// altrimenti stampa a video che “il compito è troppo complicato e gli scoccia eseguirlo”
#include <stdio.h>

int main()
{
  int num;
  printf("Inserire un numero: \n");
  scanf("%d", &num);

  if (num <= 15)
  {
    for (int i = 0; i <= 10; i++)
    {
      printf("%d x %d = %d\n", num, i, num * i);
    }
  }
  else
  {
    puts("Compito troppo complesso, mi scoccio >:(");
  }
  return 0;
}
