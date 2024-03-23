#include <cs50.h>
#include <stdio.h>

// declare function
bool valid_triangle(float sideA, float sideB, float sideC);

// define function
bool valid_triangle(float sideA, float sideB, float sideC)
{
    // check for any two side grester than the third
    if ((sideA + sideB) < sideC || (sideB + sideC) < sideA || (sideA + sideC) < sideB)
    {
        // return bool_expression
        printf("No.\n");
        return false;
    }
    // check for all positive sides
    if (sideA < 0 || sideB < 0 || sideC < 0)
    {
        // return boolean expression
        printf("No.\n");
        return false;
    }
    // return bool_expression
    return true;
}
int main(void) {}
