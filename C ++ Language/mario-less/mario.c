#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int row, s, col;

    //dont want inpt more than 8

    do
    {
        //take input
        row = get_int("rows: ");
    }
    while (row > 8 || row <= 0);
    //pattern

    for (s = 1; s <= row; s++)

    {
        //print spaces
        for (col = 1; col <= row - s; col++)
        {
            printf(" ");
        }

        //print#
        for (col = 1; col <= s; col++)
        {
            printf("#");
        }
        // bring cursor to the next line
        printf("\n");
    }

}