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
    for (int i = 0; i < height; i++)
    {
        //Note upper limit is width/2 to prevent the second half from reversing back
        //e.g. If width is 21, then block 0 will switch with 20 when j=0, but swap back when j=20
        for (int j = 0; j < width / 2; j++)
        {
            a = image[i][j].rgbtRed;
            b = image[i][j].rgbtGreen;
            c = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;

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
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            image[i][j].rgbtRed = (image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed +
            image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i][j + 1].rgbtRed +
            image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed) / 9;

            image[i][j].rgbtGreen = (image[i - 1][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen +
            image[i][j - 1].rgbtGreen + image[i][j].rgbtGreen + image[i][j + 1].rgbtGreen +
            image[i + 1][j - 1].rgbtGreen + image[i + 1][j].rgbtGreen + image[i][j + 1].rgbtGreen) / 9;

            image[i][j].rgbtBlue = (image[i - 1][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue +
            image[i][j - 1].rgbtBlue + image[i][j].rgbtBlue + image[i][j + 1].rgbtBlue +
            image[i + 1][j - 1].rgbtBlue + image[i + 1][j].rgbtBlue + image[i][j + 1].rgbtBlue) / 9;
        }
    }
    for (int k = 1; k < height - 1; k++)
    {
        image[k][0].rgbtRed = (image[k - 1][0].rgbtRed + image[k - 1][1].rgbtRed +
        image[k][0].rgbtRed + image[k][1].rgbtRed +
        image[k + 1][0].rgbtRed + image[k + 1][1].rgbtRed) / 6;

        image[k][0].rgbtGreen = (image[k - 1][0].rgbtGreen + image[k - 1][1].rgbtGreen +
        image[k][0].rgbtGreen + image[k][1].rgbtGreen +
        image[k + 1][0].rgbtGreen + image[k + 1][1].rgbtGreen) / 6;

        image[k][0].rgbtBlue = (image[k - 1][0].rgbtBlue + image[k - 1][1].rgbtBlue +
        image[k][0].rgbtBlue + image[k][1].rgbtBlue +
        image[k + 1][0].rgbtBlue + image[k + 1][1].rgbtBlue) / 6;

        image[k][width - 1].rgbtRed = (image[k - 1][width - 1].rgbtRed + image[k - 1][width - 2].rgbtRed +
        image[k][width - 1].rgbtRed + image[k][width - 2].rgbtRed +
        image[k + 1][width - 1].rgbtRed + image[k + 1][width - 2].rgbtRed) / 6;

        image[k][width - 1].rgbtGreen = (image[k - 1][width - 1].rgbtGreen + image[k - 1][width - 2].rgbtGreen +
        image[k][width - 1].rgbtGreen + image[k][width - 2].rgbtGreen +
        image[k + 1][width - 1].rgbtGreen + image[k + 1][width - 2].rgbtGreen) / 6;

        image[k][width - 1].rgbtBlue = (image[k - 1][width - 1].rgbtBlue + image[k - 1][width - 2].rgbtBlue +
        image[k][width - 1].rgbtBlue + image[k][width - 2].rgbtBlue +
        image[k + 1][width - 1].rgbtBlue + image[k + 1][width - 2].rgbtBlue) / 6;
    }

    image[0][0].rgbtRed = (image[0][0].rgbtRed + image[0][1].rgbtRed + image[1][0].rgbtRed + image[1][1].rgbtRed) / 4;
    image[0][0].rgbtGreen = (image[0][0].rgbtGreen + image[0][1].rgbtGreen + image[1][0].rgbtGreen + image[1][1].rgbtGreen) / 4;
    image[0][0].rgbtBlue = (image[0][0].rgbtBlue + image[0][1].rgbtBlue + image[1][0].rgbtBlue + image[1][1].rgbtBlue) / 4;

    image[0][width - 1].rgbtRed = (image[0][width - 1].rgbtRed + image[0][width - 2].rgbtRed + image[1][width - 1].rgbtRed + image[1][width - 2].rgbtRed) / 4;
    image[0][width - 1].rgbtGreen = (image[0][width - 1].rgbtGreen + image[0][width - 2].rgbtGreen + image[1][width - 1].rgbtGreen + image[1][width - 2].rgbtGreen) / 4;
    image[0][width - 1].rgbtBlue = (image[0][width - 1].rgbtBlue + image[0][width - 2].rgbtBlue + image[1][width - 1].rgbtBlue + image[1][width - 2].rgbtBlue) / 4;

    image[height - 1][0].rgbtRed = (image[height - 1][0].rgbtRed + image[height - 1][1].rgbtRed + image[height - 2][0].rgbtRed + image[height - 2][1].rgbtRed) / 4;
    image[height - 1][0].rgbtGreen = (image[height - 1][0].rgbtGreen + image[height - 1][1].rgbtGreen + image[height - 2][0].rgbtGreen + image[height - 2][1].rgbtGreen) / 4;
    image[height - 1][0].rgbtBlue = (image[height - 1][0].rgbtBlue + image[height - 1][1].rgbtBlue + image[height - 2][0].rgbtBlue + image[height - 2][1].rgbtBlue) / 4;

    image[height - 1][width - 1].rgbtRed = (image[height - 1][width - 1].rgbtRed + image[height - 1][width - 2].rgbtRed + image[height - 2][width - 1].rgbtRed + image[height - 2][width - 2].rgbtRed) / 4;
    image[height - 1][width - 1].rgbtGreen = (image[height - 1][width - 1].rgbtGreen + image[height - 1][width - 2].rgbtGreen + image[height - 2][width - 1].rgbtGreen + image[height - 2][width - 2].rgbtGreen) / 4;
    image[height - 1][width - 1].rgbtBlue = (image[height - 1][width - 1].rgbtBlue + image[height - 1][width - 2].rgbtBlue + image[height - 2][width - 1].rgbtBlue + image[height - 2][width - 2].rgbtBlue) / 4;

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
