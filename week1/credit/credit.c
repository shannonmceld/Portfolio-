#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt for input
    long credit = get_long ("Card Number: ");

    //get the direct placement of number
    int n1 = ((credit / ) % 10);
    int d1 = n1 * 2;

    int n2 = ((credit / 100000000000000) % 10);

    int n3 = ((credit / 10000000000000) % 10);
    int d3 = n3 * 2;

    int n4 = ((credit / 1000000000000) % 10);

    int n5 = ((credit / 100000000000) % 10);
    int d5 = n5 * 2;

    int n6 = ((credit / 10000000000) % 10);

    int n7 = ((credit / 1000000000) % 10);
    int d7 = n7 * 2;

    int n8 = ((credit / 100000000) % 10);

    int n9 = ((credit / 10000000) % 10);
    int d9 = n9 * 2;

    int n10 = ((credit / 1000000) % 10);

    int n11 = ((credit / 100000) % 10);
    int d11 = n11 * 2;

    int n12 = ((credit / 10000) % 10);

    int n13 = ((credit / 1000) % 10);
    int d13 = n13 * 2;

    int n14 = ((credit / 100) % 10);

    int n15 = ((credit / 10) % 10);
    int d15 = n15 * 2;

    int n16 = (credit % 10);

    // digit modulo
    if (d1>9)
    {d1 = d1 - 9;}
    if (d3>9)
    {d3 = d3 - 9;}
    if (d5>9)
    {d5 = d5 - 9;}
    if (d7>9)
    {d7 = d7 - 9;}
    if (d9>9)
    {d9 = d9 - 9;}
    if (d11>9)
    {d11 = d11 - 9;}
    if (d13>9)
    {d13 = d13 - 9;}
    if (d15>9)
    {d15 = d15 - 9;}

    // Luhn's Algor...
    int Alg = (d1 + d3 + d5 + d7 + d9 + d11 + d13 + d15 + n2 + n4 + n6 + n8 + n10 + n12 + n14 + n16);
    int luhn = (Alg % 10);

    if (luhn != 0)
    printf("INVALID\n");
    else
    {
    // check type of card and print
        if(n2 == 3 && (n3 == 4 || n3 == 7))
        {
            printf("AMEX\n");
        }

        else if (n1 == 5 && (n2 == 1 || n2 == 2 || n2 == 3 || n2 == 4 || n2 == 5))
        {
            printf("MASTERCARD\n");
        }
        else if (n1 == 4 || (n13 == 2))
        {
            printf("VISA\n");
        }
        else
            printf("INVALID\n");
    }

}