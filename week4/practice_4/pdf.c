#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Improper Usage. \n");
        return 1;
    }

    //opern filename
    string filename = argv[1];
    FILE *file = fopen(filename, "r");

    //check if file exist
    if (file == NULL)
    {
        printf("No such file. \n");
        return 1;
    }

    uint8_t buffer[4];
    uint8_t signature[] = {37, 80, 68, 70};

    fread (buffer, 1, 4, file);

    //does buffer signaature match?
    for (int i = 0; i < 4; i++)
    {
        if (buffer[i] != signature[i])
        {
            printf("Likely Not PDF \n");
            fclose(file);
            return 0;
        }
    }

    printf("Likely PDF! \n");
    fclose(file);
    return 0;
}