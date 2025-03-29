#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 1) Scrivere un programma che inizializzi una matrice m*n, dove m ed n sono numeri interi richiesti in input all’utente.
// 2) Tale matrice deve essere popolata con numeri random compresi tra 0 e 9.
// 3) La matrice deve poi essere stampata a video
// 4) Individua nella matrice il valore massimo ed il valore minimo, stampandoli a video insieme ai suoi riferimenti (indici di riga e di colonna)

int main()
{
  srand(time(NULL));

  int righe, colonne;
  printf("Inserire il numero di righe e colonne della matrice in ordine: ");
  scanf("%d%d", &righe, &colonne);

  int array[righe][colonne];

  int max = array[0][0];

  for (size_t i = 0; i < righe; i++)
  {
    for (size_t j = 0; j < colonne; j++)
    {
      array[i][j] = rand() % 10;
      printf("[%d]", array[i][j]);

      if (array[i][j] >= max)
      {
        max = array[i][j];
      }
    }
    puts("");
  }

  printf("Il numero più alto è: %d\n", max);
}