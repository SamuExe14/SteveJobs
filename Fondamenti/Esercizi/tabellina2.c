// Scrivi un programma che, dato in input un numero da 1 a 10, comincia a stamparne la tabellina.
// La stampa della suddetta tabellina deve interrompersi se si raggiunge un valore maggiore di 35.
// Laddove tale condizione dovesse verificarsi, stampare un messaggio in cui si spiega come mai si è interrotto, e perchè.
#include <stdio.h>

int main()
{
  printf("Inserire un numero da 1 a 10: ");
  int num;
  scanf("%d", &num);
  if (num > 0 && num <= 10)
  {
    for (int i = 0; i <= 10; i++)
    {
      if (num * i <= 35)
      {
        printf("%d x %d = %d\n", num, i, num * i);
      }
      else
      {
        puts("Il programma è stato interrotto perché il risultato supera 35");
        break;
      }
    }
  }
  else
  {
    fprintf(stderr, "È necessario inserire un numero da 1 a 10!\n");
  }
}