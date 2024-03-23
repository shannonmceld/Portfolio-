#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // ask for user input
    string text = get_string("Text: \n");

    // get each function
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);

    // calculate index
    float S = (float)((sentences / words) * 100.00) * .296;
    float l = (float)((letters / words) * 100) * 0.0588;

    float index = (l - S) - 15.8;

    // round index for the grade
    int grade = round(index);

    if (grade <= 1)
    {
        printf("Before Grade 1\n");
    }

    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }

    // else print Coleman index
    else
    {
        printf("Grade %i\n", grade);
    }
}
int count_letters(string text)
{
    int sum = 0;
    int n = strlen(text);
    // define function to count letter in above input
    for (int i = 0; i != n; i++)
    {
        if (text[i] > 64 && text[i] < 91)
        {
            sum++;
        }
        else if (text[i] > 96 && text[i] < 123)
        {
            sum++;
        }
    }
    return sum;
}
int count_words(string text)
{
    int n = strlen(text);
    int sum = 1;
    // define function to count words in the input text
    for (int i = 1; i < n; i++)
    {
        if (text[i] == 32)
        {
            sum++;
        }
    }
    return sum;
}
int count_sentences(string text)
{
    int n = strlen(text);
    int sum = 0;
    // define function to count sentences in the input text
    for (int i = 0; i < n; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sum++;
        }
    }
    return sum;
}
