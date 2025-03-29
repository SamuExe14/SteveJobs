// Scrivi un programma che, partendo da a=2
// aggiunga ad a 1 ad ogni iterazione, fin quando l’utente non decida di uscire
#include <stdio.h>

int main()
{
  int a = 2;
  char risposta;

  while (a)
  {
    printf("%d\n", a);
    risposta = getchar();

    printf("Vuoi continuare? [s/n]: \n");
    if (risposta == 'n')
      break;

    ++a;
  }
}