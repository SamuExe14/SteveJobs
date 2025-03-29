#include <stdio.h>
#include <stdlib.h>

int main()
{
  float reddito;
  printf("Immettere il proprio reddito annuale: ");
  scanf("%f", &reddito);

  if ((reddito / reddito) != 1) // controllo che stia venendo immesso un numero
  {
    fprintf(stderr, "È necessario immettere un valore numerico\n"); // stampo un errore nello stream stderr
    exit(EXIT_FAILURE);                                             // gestisco il codice d'uscita
  }

  if (reddito >= 0 && reddito < 10000) // effettuo i diversi controlli
  {
    puts("Reddito in fascia 1");
  }
  else if (reddito > 10000 && reddito <= 20000)
  {
    puts("Reddito in fascia 2");
  }
  else
  {
    puts("Reddito in fascia 3");
  }
}