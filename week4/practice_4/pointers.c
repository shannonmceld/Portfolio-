#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main (void)
{
int a = 28;
int b = 50;
int *c = &a;

*c = 14;
c = &b;
*c = 25;

}