#include "helpers.h"
#include "stdio.h"

void convert(int height, int width, RGBTRIPLE image[height][width])
{
    int red[height][width];
    int green[height][width];
    int blue[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red[i][j] = image[i][j].rgbtRed;
            green[i][j] = image[i][j].rgbtGreen;
            blue[i][j] = image[i][j].rgbtBlue;
        }
    }
    return;
}

void convert_back(int height, int width, RGBTRIPLE image[height][width])
{
    int red[height][width];
    int green[height][width];
    int blue[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = red[i][j];
            image[i][j].rgbtGreen = green[i][j];
            image[i][j].rgbtBlue = blue[i][j];
        }
    }
    return;
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

void reflect_function(int height, int width, int array[height][width])
{
    //Temporarily store values in x
    int x = 0;
    for (int i = 0; i < height; i++)
    {
        //Note upper limit is width/2 to prevent the second half from reversing back
        //e.g. If width is 21, then block 0 will switch with 20 when j=0, but swap back when j=20
        for (int j = 0; j < width / 2; j++)
        {
            x = array[i][j];

            array[i][j] = array[i][width - 1 - j];

            array[i][width - 1 - j] = x;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int red[height][width];
    int green[height][width];
    int blue[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red[i][j] = image[i][j].rgbtRed;
            green[i][j] = image[i][j].rgbtGreen;
            blue[i][j] = image[i][j].rgbtBlue;
        }
    }
    
    reflect_function(height, width, red);
    reflect_function(height, width, green);
    reflect_function(height, width, blue);
    convert_back(height, width, image);
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
