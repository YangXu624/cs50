#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Temporarily store values in a, b, and c
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int e = 0;
    int f = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            a = image[i][j].rgbtRed;
            b = image[i][j].rgbtGreen;
            c = image[i][j].rgbtBlue;

            d = image[i][width - 1 - j].rgbtRed;
            e = image[i][width - 1 - j].rgbtGreen;
            f = image[i][width - 1 - j].rgbtBlue;

            image[i][j].rgbtRed = d;
            image[i][j].rgbtGreen = e;
            image[i][j].rgbtBlue = f;

            image[i][width - 1 - j].rgbtRed = a;
            image[i][width - 1 - j].rgbtGreen = b;
            image[i][width - 1 - j].rgbtBlue = c;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
