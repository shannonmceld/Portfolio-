#include <ctyp.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


/*Notice that strcpy does the same work that our for loop previously did.

Both get_string and malloc return NULL, a special value in memory, in the event that something goes wrong.
You can write code that can check for this NULL condition as follows:
Notice that if the string obtained is of length 0 or malloc fails, NULL is returned.
Further, notice that free lets the computer know you are done with this block of memory you created via malloc.*/

int main(void)
{
    // Get a string
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Free memory
    free(t);
    return 0;
}