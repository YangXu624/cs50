#include "helpers.h"
#include <math.h>
#include <stdlib.h>

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
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp[i][j];
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
            float counter = 0.00;
            int totalR, totalG, totalB;
            totalR = totalG = totalB = 0;

            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    int coord_y = i + y;
                    int coord_x = j + x;

                    if ((coord_y < 0 || coord_y > height - 1) || (coord_x < 0 || coord_x > width - 1))
                    {
                        continue;
                    }

                    totalR += image[coord_y][coord_x].R;
                    totalG += image[coord_y][coord_x].G;
                    totalB += image[coord_y][coord_x].B;
                    counter++;
                }
            }
            temp[i][j].R = round(totalR / counter);
            temp[i][j].G = round(totalG / counter);
            temp[i][j].B = round(totalB / counter);
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
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float GxR, GxG, GxB, GyR, GyG, GyB;
            GxR = GxG = GxB = GyR = GyG = GyB = 0.00;
            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    int coord_y = i + y;
                    int coord_x = j + x;

                    if (coord_y < 0 || coord_y > height - 1 || coord_x < 0 || coord_x > width - 1)
                    {
                        continue;
                    }

                    GxR = GxR + (x * (2 - abs(y)) * image[coord_y][coord_x].R);
                    GxG = GxG + (x * (2 - abs(y)) * image[coord_y][coord_x].G);
                    GxB = GxB + (x * (2 - abs(y)) * image[coord_y][coord_x].B);

                    GyR = GyR + (y * (2 - abs(x)) * image[coord_y][coord_x].R);
                    GyG = GyG + (y * (2 - abs(x)) * image[coord_y][coord_x].G);
                    GyB = GyB + (y * (2 - abs(x)) * image[coord_y][coord_x].B);
                }
            }
            temp[i][j].R = fmin(round(sqrt(GxR * GxR + GyR * GyR)), 255);
            temp[i][j].G = fmin(round(sqrt(GxG * GxG + GyG * GyG)), 255);
            temp[i][j].B = fmin(round(sqrt(GxB * GxB + GyB * GyB)), 255);

            // Unsolved question: Why does "if (temp[][] > 255) {temp[][] = 255;}" yield different results?
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
