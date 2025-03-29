//? Inizializza un array di dimensione 100 con numeri random, compresi in un intervallo da 0 a 255.
//? -Individuane il massimo ed il minimo
//? -calcola la media dei valori dell’array
//? -Individua il numero che compare piu’ frequentemente

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define SIZE 100

void randomizza_array(int array[])
{
  srand(time(NULL));
  for (size_t i = 0; i <= 100; i++)
  {
    array[i] = rand() % 256;
    // printf("%d ", array[i]);
  }
}

void trova_max(int array[])
{
  int min, max;

  max = array[0];
  min = array[0];

  for (size_t x = 0; x < 100; ++x)
  {
    if (array[x] > max)
    {
      max = array[x];
    }
    else if (array[x] < min)
    {
      min = array[x];
    }
  }
  printf("Il numero minimo nell'array è: %d\nIl numero massimo nell'array è: %d", min, max);
}

void somma_media(int array[])
{
  int somma = 0;
  for (size_t j = 0; j < 100; j++)
  {
    somma += array[j];
  }

  float media = (float)somma / SIZE;

  printf("\nLa somma degli elementi dell'array è: %d\n", somma);
  printf("La media dell'array è: %.2f\n", media);
}

void ottieni_frequenza(int array[], int frequenza[])
{
  for (size_t i = 0; i < 100; i++)
  {
    frequenza[array[i]]++;
    // printf("%d %lu\n", frequenza[array[i]], i);
  }
}

void bubblesort(int array[])
{
  int appoggio;

  for (size_t i = 0; i < 7; i++)
  {
    for (size_t j = 0; j < 7; j++)
    {
      if (array[j] < array[j + 1])
      {
        appoggio = array[j];
        array[j] = array[j + 1];
        array[j + 1] = appoggio;
      }
    }
  }
}

void numeri_frequenti(int frequenza[])
{
  int numeriFrequenti[2][10] = {0};

  // for (size_t i = 0; i < 255; i++)
  // {
  //   for (size_t j = 0; j < 2; j++)
  //   {
  //     for (size_t x = 0; x < 10; x++)
  //     {
  //       if (frequenza[i] > numeriFrequenti[j][j]) // FIXME
  //       {
  //         numeriFrequenti[j][x] = i;
  //         numeriFrequenti[j + 1][x] = i;
  //       }
  //     }
  //   }
  // }

  for (size_t i = 0; i < 2; i++)
  {
    for (size_t j = 0; j < 10; j++)
    {
      printf("%d ", numeriFrequenti[i][j]); // TODO da completare
    }
    puts("");
  }
}

int main()
{
  int array[SIZE];
  int frequenzaNumeri[255] = {0};

  randomizza_array(array);
  trova_max(array);

  somma_media(array);

  // stila la classifica dei 10 valori piu frequenti, e stampali in ordine decrescente in frequenza ,
  // stampandone(int array[]){} anche la frequenza, in caso di frequenze uguali è preferibile il piu piccolo.

  ottieni_frequenza(array, frequenzaNumeri);
  numeri_frequenti(frequenzaNumeri);
}