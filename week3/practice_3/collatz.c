#include <cs50.h>
#include <stdio.h>

int collatz(int n);

int main(void)
{
    int number = get_int("number: \n");
    int integar = collatz(number);
    printf("return: %i\n", integar);

}

int collatz(int n)
{
    int odd = (n %2 == 1);
    int even = (n %2 == 0);

    if (n == 1)
        return 0;
    else if (even)
        return 1 + collatz(n/2);
    else
        return 1 + collatz(3 * n + 1);

}

  int vote_total = 0;
    int i = 0;
    for (i = 0; i < candidate_count; i++)
    {
         if (candidates[i].votes > vote_total)
        {
            vote_total = candidates[i].votes;
        }
    }

    for (i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == vote_total)
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}