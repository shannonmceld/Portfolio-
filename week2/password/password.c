// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    if(strlen(password) <= 8)
    {
        return false;
    }
    int v =strlen(password);
    for (int i = 0; i < v; i++)
        {
            if((password[v]>= 'a' && password[v] <= 'z') && (password[v] >= 'A' && password[v] <= 'Z') && (password[v] >= '0' && password[v] <= '9') && (password[v] >= '!' && password[v] <= '/'))

        }
        return true;
}