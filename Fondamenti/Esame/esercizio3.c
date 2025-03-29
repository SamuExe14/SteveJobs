#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  srand(time(NULL)); // imposto il mio timer al 1/1/1970
  int array[7][8];
  int pari = 0;
  int dispari = 0;

  puts("L'array con numeri random risulta essere: ");
  for (size_t i = 0; i < 7; i++)
  {
    for (size_t j = 0; j < 8; j++)
    {
      array[i][j] = rand() % 4;   // riempio l'array con numeri random
      printf("%d ", array[i][j]); // e lo stampo contemporaneamente
    }
    puts("");
  }

  for (size_t i = 0; i < 7; i++)
  {
    for (size_t j = 0; j < 8; j++)
    {
      if (i % 2 == 0 && array[i][j] % 2 == 0) // conto se nelle righe pari ci sono numeri pari
      {
        pari++;
      }
      else if (i % 2 == 1 && array[i][j] % 2 == 1) // viceversa nelle righe dispari
      {
        dispari++;
      }
    }
  }
  printf("\nNell'array ci sono %d numeri pari nelle righe pari e %d numeri dispari nelle righe dispari\n\n", pari, dispari);

  puts("Array finale con elevamento a potenza");
  for (size_t i = 0; i < 7; i++)
  {
    for (size_t j = 0; j < 8; j++)
    {
      if ((i + j) % 2 == 0)
      {
        array[i][j] *= array[i][j]; // elebo alla 2 se i + j è pari
      }
      else
      {
        array[i][j] = array[i][j] * array[i][j] * array[i][j]; // elevo alla 3 se i + j è dispari
      }
      printf("%d ", array[i][j]);
    }
    puts("");
  }
}