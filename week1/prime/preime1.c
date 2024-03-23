#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n , i =0, flag = 0;

    if (n == 0 || n == 1)
    flag = 1;
    for (i = 2; i <= n /2; ++i)
    {
        if (n% i ==0)
        {
            flag =1;
            break;
        }
    }

    if (flag == 0)
     printf("%d\n is a prime number.", n);
     else
     printf("%d\n is not a prime number. ",n);
     return 0;
}