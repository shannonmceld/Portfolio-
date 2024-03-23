//recover files off memory card
#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    typedef uint8_t BYTE;
    BYTE buffer[512];
    char filename[8];
    int flag = 0;
    FILE *IMAGE = NULL;
    //opern memory card
    FILE *raw_card = fopen(argv[1], "r");
    if (argc != 2)
    {
        printf("\nUsage: ./recover Image. \n");
        return 1;
    }

    //check if file exist
    if (raw_card == NULL)
    {
        printf("Recover card.raw \n");
        return 1;
    }
    //loop reading
    while (!(false))
    {
        int read_card = fread(buffer, sizeof(BYTE), 512, raw_card);
        // Ensure rawfile is (likely) a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & (0xf0)))
        {
            //flag each JPEG to count filename
            if (flag == 0)
            {
                sprintf(filename, "%03i.jpg", flag);
                IMAGE = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), read_card, IMAGE);
                flag++;
            }

            else
            {
                //close previos file  and count JPEG
                fclose(IMAGE);
                sprintf(filename, "%03i.jpg", flag);
                IMAGE = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), read_card, IMAGE);
                flag++;
            }
        }
        //make sure it only read JPEG
        else if (flag != 0)
        {
            fwrite(buffer, sizeof(BYTE), read_card, IMAGE);
            if (read_card == 0)
            {
                fclose(IMAGE);
                fclose(raw_card);
                return 0;
            }
        }
    }
    //close all files
    fclose(IMAGE);
    fclose(raw_card);
}

