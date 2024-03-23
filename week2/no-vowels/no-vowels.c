// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


string replace(string word);


int main(int argc, string argv[])
{
    //single command-line argument, that convert word.
    string vowels = replace(argv[1]);
    if (argc != 2)
    {
        //print error if no command line argument
        printf("Missing command_line argument\n");
        return 1;
    }
    else
    {
        printf("%s \n", vowels);
    }
}
//replace function
string replace(string word)
{
    int n = strlen(word);

    //loop that replace vowels to number
    for (int i = 0; i < n; i++)
    {
        //variables to changer words to upper or lower
        char vowel = tolower(word[i]);
        char vowels = toupper(word[i]);

        //condition that checks if word is lower
        if (islower(word[i]))
        {
            switch (vowel)
            {
                case 'a':
                    word[i] = '6';
                    break;
                case 'e':
                    word[i] = '3';
                    break;
                case 'i':
                    word[i] = '1';
                    break;
                case 'o':
                    word[i] = '0';
                    break;
                default:
                    word[i] = vowel;
                    break;
            }
        }
        //condition that checks if word is upper
        if (isupper(word[i]))
        {
            switch (vowel)
            {
                case 'A':
                    word[i] = '6';
                    break;
                case 'E':
                    word[i] = '3';
                    break;
                case 'I':
                    word[i] = '1';
                    break;
                case 'O':
                    word[i] = '0';
                    break;
                default:
                    word[i] = vowels;
                    break;
            }
        }
    }
    //return change word
    return word;
}