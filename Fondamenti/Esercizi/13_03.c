// ESERCIZIO MENU
//  Scrivere un programma che mostri un menu elettronico con tre opzioni di cibo e un'opzione di uscita.
//  L'utente può selezionare più prodotti e, quando sceglie di uscire, il programma stampa il totale da pagare.

#include <stdio.h>

void stampaMenu(void)
{
  printf("Selezionare il cibo desiderato: \na) Pollo\nb) Pizza\nc) Kebab\nd) Fine del programma\n");
}

int main()
{
  char scelta;
  float totale_conto = 0;

  do
  {
    stampaMenu();
    scanf("%c", &scelta);
    switch (scelta)
    {
    case 'a':
      printf("Pollo aggiunto nel carrello\n");
      totale_conto += 5.99;
      break;
    case 'b':
      printf("Pizza aggiunta nel carrello\n");
      totale_conto += 7.99;
      break;
    case 'c':
      printf("Kebab aggiunto nel carrello\n");
      totale_conto += 7.50;
      break;
    case '\n':
    case '\t':
    case ' ':
    case 'd':
      break;
    default:
      fprintf(stderr, "Inserire un'opzione tra quelle elencate");
      break;
    }
  } while (scelta != 'd');

  printf("Il totale del carrello\n è %.2f, carta o contanti?\n", totale_conto);
}