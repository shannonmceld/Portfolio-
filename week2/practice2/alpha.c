#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //get user input
    string word = get_string("Word: ");

    //create length of user input
    int word_length = strlen(word);
    {

        //loop to check each letter alphabeticallhy
     for (int i = 0; i < word_length - 1; i++)
        //create condition
        if (word[i] > word[i+1])
        {
            printf("no\n");
            return 0;
        }
    }

    printf("yes\n");
    return 0;
}