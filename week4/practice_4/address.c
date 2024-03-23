#include <stdio.h>

/* pointer is a variable that contains the address of some value.
Most succinctly, a pointer is an address in your computer’s memory.*/

int main(void)
{
    int n = 50
    int *p = &n;
    printf("%p\n", p);
}