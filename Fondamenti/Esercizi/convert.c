#include <stdio.h>

/*
Esercizio 2: Convertitore di Temperatura
Crea un programma che converta una temperatura da Celsius a Fahrenheit o da Fahrenheit a Celsius.

Usa una funzione convertiTemperatura() che prenda in input la temperatura e la conversione da fare.
L'utente sceglie con uno switch quale conversione eseguire.
Se l'utente inserisce un'opzione non valida, il programma deve segnalarlo.

Formula di conversione:
Da Celsius a Fahrenheit: F = (C × 9/5) + 32
Da Fahrenheit a Celsius: C = (F - 32) × 5/9
*/

void convertiTemperatura(int scelta)
{
  float temperatura;
  puts("Inserire temperatura da convertire");
  scanf("%f", &temperatura);

  if (scelta == 1)
  {
    temperatura = temperatura * ((float)9 / 5) + 32;
    printf("La temperatura convertita è %.f F˚\n", temperatura);
  }
  else
  {
    temperatura = (temperatura - 32) * ((float)5 / 9);
    printf("La temperatura convertita è %.f C˚\n", temperatura);
  }
}

int main()
{
  int scelta;
  float temperatura;
  // puts("Selezionare tipo di conversione:");
  // puts("1) Celsius a Fahrenheit\n2) Fahrenheit a Celsius");

  // while ((scelta = getchar()) != EOF)
  while (scelta != -1)
  {
    puts("Selezionare tipo di conversione:");
    puts("1) Celsius a Fahrenheit\n2) Fahrenheit a Celsius");
    scanf("%d", &scelta);

    switch (scelta)
    {

    case 1: // Celsius --> Fahrenheit
      convertiTemperatura(scelta);
      break;

    case 2: // Fahrenheit --> Celsius
      convertiTemperatura(scelta);
      break;

    case '\n':
    case '\t':
    case ' ':
    case '\\':
      break;

    default:
      puts("\nSCELTA NON VALIDA!");
      puts("Inserire un dato valido\n");
      break;
    }
  }
  return 0;
}