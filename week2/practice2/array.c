#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int length;

    do
    {
        // get size of array
        length = get_int("length:  ");
    }
    while (length < 1);
    //name array
    int Dou[length];

    //give array a value
    Dou[0] = 1;
    //print out
    printf("%i\n", Dou[0]);

    for (int i = 1; i < length; i++)
    {
        Dou[i] = (Dou[i - 1]);
        printf("%i \n", Dou[i]);
    }


}