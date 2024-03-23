#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

/*Notice that string t = s copies the address of s to t. This does not accomplish what we are desiring.
The string is not copied – only the address is.

Before we address this challenge, it’s important to ensure that we don’t experience a segmentation fault through our code,
where we attempt to copy string s to string t, where string t does not exist.
We can employ the strlen function as follows to assist with that:*/

//Notice that strlen is used to make sure string t exists. If it does not, nothing will be copied.

int main(void)
{
    // Get a string
    string s = get_string("s: ");

    // Copy string's address
    string t = s;

    // Capitalize first letter in string
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}




/*Notice that s and t are still pointing at the same blocks of memory.
This is not an authentic copy of a string. Instead, these are two pointers pointing at the same string.

To be able to make an authentic copy of the string, we will need to introduce two new building blocks.
First, malloc allows you, the programmer, to allocate a block of a specific size of memory.
Second, free allows you to tell the compiler to free up that block of memory you previously allocated.
Notice that n = strlen(s) is defined now in the left-hand side of the for loop.
It’s best not to call unneeded functions in the middle condition of the for loop, as it will run over and over again.
When moving n = strlen(s) to the left-hand side, the function strlen only runs once.*/
/*
int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory, including '\0'
    for (int i = 0; i <= strlen(s); i++)
    {
        t[i] = s[i];
    }

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}*/