#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(int argc, string argv[])
{
    int i = 0;
    string ciphertext = argv[1];
    // lack of argument
    if (argc == 1)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // to many arguments
    if (argc > 2)
    {
        printf("1 2 3 \nUsage: ./substitution key");
        return 1;
    }
    // ensure argv have 26 characters
    if (strlen(argv[1]) != 26)
    {
        printf("ABC \nKey must contains 26 characters.\n");
        return 1;
    }
    else
    {
        //valid characters,
        bool valid = false;
        for (i = 0; i < strlen(argv[1]); i++)
        {
            for (int k = i + 1 ; k < strlen(argv[1]) + 1 ; k++)
            {
                //handles duplicate lowere and uppercase
                if (isalpha(argv[1][i]) && tolower(argv[1][i]) != tolower(argv[1][k]))
                {
                    valid = true;
                }
                else
                {
                    printf("Usage: ./substitution key\n");
                    return 1;
                }
            }

        }

        //get plaintext
        string plaintext = get_string("plaintext:\n");
        int o = strlen(plaintext);
        //encryption
        for (i = 0; i < o; i++)
        {
            if (isupper(plaintext[i]))
            {
                plaintext[i] = toupper(argv[1][plaintext[i] - 65]);
            }
            else if (islower(plaintext[i]))
            {
                plaintext[i] = tolower(argv[1][plaintext[i] - 97]);
            }
        }
        //output cyphertext
        printf("ciphertext: %s\n", plaintext);
        return 0;
    }
}

