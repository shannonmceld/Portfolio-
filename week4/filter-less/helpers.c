#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    /*Calculate the average pixel value
    set each color value to the average value
    round to the nearest integer*/

    float avgvalue;
    for (int i = 0; i < height; i ++)
    {
        for (int j = 0; j < width; j ++)
        {
            avgvalue = (float)(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;
            int roundedavgvalue = round(avgvalue);
            //set each color value to the average value
            image[i][j].rgbtRed = roundedavgvalue;
            image[i][j].rgbtGreen = roundedavgvalue;
            image[i][j].rgbtBlue = roundedavgvalue;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    /*Calculate each new color value using Seepha formula
    if value is more than 255 cap the value*/
    float sepRed, sepGreen, sepBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepRed = (round)((image[i][j].rgbtRed * .393) + (image[i][j].rgbtGreen * .769) + (image[i][j].rgbtBlue * .189));
            sepGreen = (round)((image[i][j].rgbtRed * .349) + (image[i][j].rgbtGreen * .686) + (image[i][j].rgbtBlue * .168));
            sepBlue = (round)((image[i][j].rgbtRed * .272) + (image[i][j].rgbtGreen * .534) + (image[i][j].rgbtBlue * .131));
            // cap the value
            image[i][j].rgbtRed = sepRed > 255 ? 255 : sepRed;
            image[i][j].rgbtGreen = sepGreen > 255 ? 255 : sepGreen;
            image[i][j].rgbtBlue = sepBlue > 255 ? 255 : sepBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    /*swap each pixel on horizonally opposite sides*/
    RGBTRIPLE mirror[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            mirror[i][j] = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = mirror[i][j];
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    /*blur all the pixel w/i one row and one column
    calculate the average amount of RGB*/
    RGBTRIPLE blur[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            blur[i][j] = image[i][j];
        }
    }

    float pixelRed = 0;
    float pixelGreen = 0;
    float pixelBlue = 0;
    int flag = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get the pixel w/i one row and one column
            for (int x = i - 1; x <= i + 1; x++)
            {
                for (int y = j - 1; y <= j + 1; y++)
                {
                    if (y < width && x < height && y >= 0 && x >= 0)
                    {
                        //set the temp value to equal the temp axal
                        pixelRed += blur[x][y].rgbtRed;
                        pixelGreen += blur[x][y].rgbtGreen;
                        pixelBlue += blur[x][y].rgbtBlue;
                        flag++;
                    }
                }
            }
            //set the original value to eual the temp valuwe
            image[i][j].rgbtRed = round(pixelRed / flag);
            image[i][j].rgbtGreen = round(pixelGreen / flag);
            image[i][j].rgbtBlue = round(pixelBlue / flag);
            flag = 0;
            pixelRed = pixelGreen = pixelBlue = 0;
        }
    }
    return;
}
