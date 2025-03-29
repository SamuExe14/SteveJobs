#include <stdio.h>

int main()
{
  for (size_t i = 1; i <= 10; i++)
  {
    printf("3 x %lu = %lu\n", i, 3 * i);
  }

  printf("###############################\n");

  int a = 3;
  while (a <= 37)
  {
    printf("Il valore di a è %d\n", a);
    a += 4;
  }

  int num;
  puts("#########################################");
  puts("Inserire un numero");

  scanf("%d", &num);
  for (size_t i = 0; i <= 10; i++)
  {
    printf("%d x %lu = %d\n", num, i, num * (int)i);
  }
}