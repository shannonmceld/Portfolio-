#include <cs50.h>
#include <stdio.h>

int main(void)
{

    string answer = get_string("name:");

    int age = get_int("age: ");

    string pn = get_string("phone number: ");

    printf("name: %s\n. age: %i\n. phone number: %s\n. ", answer, age, pn);

 }