#include "helpers.h"
#include <math.h>

#define R rgbtRed
#define G rgbtGreen
#define B rgbtBlue

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].R;
            float green = image[i][j].G;
            float blue = image[i][j].B;

            image[i][j].R = image[i][j].G = image[i][j].B = round((red + green + blue) / 3);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp[i][j] = image[i][j];
            image[i][j] = image[i][width - j];
            image[i][width - j] = temp[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int counter = 0;

            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    int coord_y = i + y;
                    int coord_x = j + x;

                    if ((coord_y < 0 || coord_y > height) || (coord_x < 0 || coord_x > width))
                    {
                        continue;
                    }

                    temp[i][j].R += image[coord_y][coord_x].R;
                    temp[i][j].G += image[coord_y][coord_x].G;
                    temp[i][j].B += image[coord_y][coord_x].B;
                    counter++;
                }
            }
            float red = temp[i][j].R;
            float green = temp[i][j].G;
            float blue = temp[i][j].B;
            temp[i][j].R = round(red / counter);
            temp[i][j].G = round(green / counter);
            temp[i][j].B = round(blue / counter);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
