#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>



//FORMULA
    float l = (letter/ space) * 100.00;
    float s  = (punct / space) * 100.0;
    float index = (0.0588 * l) - (0.296 * s) -15.8;
    int round_index = round(index);