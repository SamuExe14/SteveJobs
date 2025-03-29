#include <stdio.h>

int main()
{
  //! CONFRONTO

  int x, y;
  puts("Inserire due numeri per determinarne il maggiore");
  scanf("%d%d", &x, &y);

  if (x < y)
  {
    printf("%d è il più grande\n", y);
  }
  else if (x > y)
  {
    printf("%d è il più grande\n", x);
  }
  else
  {
    puts("I numeri sono uguali");
  }

  //! SCONTO

  float spesa;
  puts("A quanto ammonta il totale della spesa?");
  scanf("%f", &spesa);

  if (spesa > 100 && spesa < 300)
  {
    spesa -= (spesa * 0.05);
    puts("È stato applicato uno sconto del \%5 al prezzo totale");
  }
  else if (spesa > 300)
  {
    spesa -= (spesa * 0.1);
    puts("È stato applicato uno sconto del \%10 al prezzo totale");
  }

  //! TRE NUMERI

  int a, b, c;
  puts("Inserire tre numeri interi");
  scanf("%d%d%d", &a, &b, &c);

  if (a == b && c == a)
  {
    puts("Tutti uguali");
  }
  else if ((a == b && a != c) || (b == c && b != a) || (a == c && b != c))
  {
    puts("Due uguali e uno diverso");
  }
  else
    puts("Tutti diversi");

  //! MENÙ SCELTA
  puts("MENÙ DI PROVA - premere:\n");
  puts("a) Per immettere dati\nb) Per determinare il maggiore");
  puts("c) Per determinare il minore\nd) Per ordinare");
  puts("e) Per visualizzare");

  char scelta;
  scanf("%c", &scelta);

  switch (scelta)
  {
    int numerox, numeroy;

  case 'a':
    puts("In esecuzione l'opzione a");
    break;
  case 'b':
    puts("In esecuzione l'opzione b");
    break;
  case 'c':
    puts("In esecuzione l'opzione c");
    break;
  case 'd':
    puts("In esecuzione l'opzione d");
    break;
  case 'e':
    puts("In esecuzione l'opzione e");
    break;
  case '\n':
  case '\t':
  case ' ':
    break;
  default:
    puts("Opzione Inesistente");
    break;
  }

  //! IDRAULICO
}