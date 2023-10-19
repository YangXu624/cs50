#include "helpers.h"

#define R rgbtRed
#define G rgbtGreen
#define B rgbtBlue

#define REFLECT(R)
(
    reflect2
)

#define APPLY(FUNCTION)
(
    FUNCTION(R)
    FUNCTION(G)
    FUNCTION(B)
)

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = (image[i][j].R + image[i][j].G + image[i][j].B) / 3;
            image[i][j].R = average;
            image[i][j].G = average;
            image[i][j].B = average;
        }
    }
    return;
}

void reflect2(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            image[i][j].R = image[i][width - j].R;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    APPLY(REFLECT)
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
