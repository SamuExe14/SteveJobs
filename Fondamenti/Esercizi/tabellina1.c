#include <stdio.h>

int main()
{
  for (int i = 1; i <= 9; i++)
  {
    if (i % 2 == 1)
    {
      for (int j = 0; j <= 10; j++)
      {
        printf("%d x %d = %d\n", i, j, i * j);
      }
      puts("#########");
    }
  }
}