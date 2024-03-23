/* #include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
}*/

/*Notice that running this program does not cause any errors.
While malloc is used to allocate enough memory for an array, the code fails to free that allocated memory.
If you type make memory followed by valgrind ./memory,
you will get a report from valgrind that will report where memory has been lost as a result of your program.
You can modify your code as follows:*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
    free(x);
}