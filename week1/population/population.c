#include <cs50.h>
#include <stdio.h>

int main(void)
   // TODO: Prompt for start size
{
    int start;
    do
    {
        start = get_int("population size: ");
    }

     while (start < 9);

     int end;
     do
     {
        end = get_int("end Size: ");
     }

     while (end < 10);

     int year = 0;
     while (start < end)
     {
        start += start / 12;
        year++;
     }
      printf("Year: %i\n", year);
}