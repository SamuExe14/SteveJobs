#include <stdio.h>
#include <stdlib.h>

void menu() // funzione per la stampa del menù
{
  puts("\nScegliere una delle seguenti opzioni: ");
  puts("1) Addizione");
  puts("2) Sottrazione");
  puts("3) Moltiplicazione");
  puts("4) Divisione");
  puts("5) Termina il programma");
}

int addizione(int addendo1, int addendo2) // definisco e implemento le funzioni
{
  return addendo1 + addendo2;
}

int sottrazione(int minuendo, int sottraendo)
{
  return minuendo - sottraendo;
}

int moltiplicazione(int operatore1, int operatore2)
{
  return operatore1 * operatore2;
}

float divisione(int operatore1, int operatore2)
{
  return (float)operatore1 / operatore2;
}

int main()
{
  puts("############CALCOLATRICE############");

  int selezione;
  int counter = 0;
  int successo = 0;

  do
  {
    menu();
    scanf("%d", &selezione);
    int operando, operatore;

    switch (selezione) // switch nella selezione dell'utente
    {
    case 1: // addizione
      printf("Inserire due numeri: ");
      scanf("%d%d", &operando, &operatore);
      printf("Il risultato dell'addizione è: %d\n", addizione(operando, operatore));
      counter++;
      successo++;
      break;

    case 2: // sottrazione
      printf("Inserire due numeri: ");
      scanf("%d%d", &operando, &operatore);
      printf("Il risultato della sottrazione è: %d\n", sottrazione(operando, operatore));
      counter++;
      successo++;
      break;

    case 3: // moltiplicazione
      printf("Inserire due numeri: ");
      scanf("%d%d", &operando, &operatore);
      printf("Il risultato della moltiplicazione è: %d ", moltiplicazione(operando, operatore));
      counter++;
      successo++;
      break;

    case 4: // divisione
      printf("Inserire due numeri: ");
      scanf("%d%d", &operando, &operatore);
      if (operatore == 0) // controllo se sta per essere eseguita una divisione per 0
      {
        puts("ERRORE, non è possibile effettuare una divisione per 0");
        counter++;
        break;
      }
      printf("Il risultato della divisione è: %.2f\n", divisione(operando, operatore));
      counter++;
      successo++;
      break;

    case 5: // terminazione del programma
      puts("PROGRAMMA TERMINATO CON SUCCESSO");
      printf("Il programma è stato ripetuto %d volte\n", counter);
      printf("e %d volte è stata eseguita un'operazione con successo, ciao!\n", successo);
      exit(EXIT_SUCCESS); // gestisco il codice d'uscita
      break;

    case ' ': // ignora i caratteri come spazio, newline o tab
    case '\n':
    case '\t':
      break;

    default: // se non viene selezionata l'operazione corretta riparte dal menù
      puts("È necessario inserire un'opzione tra quelle riportate");
      counter++;
      break;
    }
  } while (selezione != 5);
}