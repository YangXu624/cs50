#include "helpers.h"

#define R rgbtRed
#define G rgbtGreen
#define B rgbtBlue

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
    int average = 0;
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
    convert(height, width, image);
    reflect_function(height, width, red);
    reflect_function(height, width, green);
    reflect_function(height, width, blue);
    convert_back(height, width, image);
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
    //On hind sight, there was no need to brute force through
    //Could have just did the first two 'for loops'
    //Then applied x9/4 for 4 corner pixels, and x9/6 for edge pieces
    return;
    //On hind sight of hind sight, I could have wrote a function to process everything.. bruh
    //Will come back to write this function
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int new_pixel_rx[height][width], new_pixel_ry[height][width];
    int new_pixel_gx[height][width], new_pixel_gy[height][width];
    int new_pixel_bx[height][width], new_pixel_by[height][width];
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            new_pixel_rx[i][j] = pow(((-1)*(image[i - 1][j - 1].rgbtRed) + (-2)*(image[i][j - 1].rgbtRed) +
            (-1)*(image[i + 1][j - 1].rgbtRed) + (image[i - 1][j + 1].rgbtRed) + (2)*(image[i][j + 1].rgbtRed) +
            (image[i + 1][j + 1].rgbtRed)), 2);

            new_pixel_rx[i][j] = pow(((-1)*(image[i - 1][j - 1].rgbtGreen) + (-2)*(image[i][j - 1].rgbtGreen) +
            (-1)*(image[i + 1][j - 1].rgbtGreen) + (image[i - 1][j + 1].rgbtGreen) + (2)*(image[i][j + 1].rgbtGreen) +
            (image[i + 1][j + 1].rgbtGreen)), 2);

            new_pixel_rx[i][j] = pow(((-1)*(image[i - 1][j - 1].rgbtBlue) + (-2)*(image[i][j - 1].rgbtBlue) +
            (-1)*(image[i + 1][j - 1].rgbtBlue) + (image[i - 1][j + 1].rgbtBlue) + (2)*(image[i][j + 1].rgbtBlue) +
            (image[i + 1][j + 1].rgbtBlue)), 2);
        }
    }

    for (int i = 1; i < width - 1; i++)
    {
        for (int j = 1; j < height - 1; j++)
        {
            new_pixel_ry[i][j] = pow(((-1)*(image[j - 1][i - 1].rgbtRed) + (-2)*(image[j - 1][i].rgbtRed) +
            (-1)*(image[j - 1][i + 1].rgbtRed) + (image[j + 1][i - 1].rgbtRed) + (2)*(image[j + 1][i].rgbtRed) +
            (image[j + 1][i + 1].rgbtRed)), 2);

            new_pixel_ry[i][j] = pow(((-1)*(image[j - 1][i - 1].rgbtGreen) + (-2)*(image[j - 1][i].rgbtGreen) +
            (-1)*(image[j - 1][i + 1].rgbtGreen) + (image[j + 1][i - 1].rgbtGreen) + (2)*(image[j + 1][i].rgbtGreen) +
            (image[j + 1][i + 1].rgbtGreen)), 2);

            new_pixel_ry[i][j] = pow(((-1)*(image[j - 1][i - 1].rgbtBlue) + (-2)*(image[j - 1][i].rgbtBlue) +
            (-1)*(image[j - 1][i + 1].rgbtBlue) + (image[j + 1][i - 1].rgbtBlue) + (2)*(image[j + 1][i].rgbtBlue) +
            (image[j + 1][i + 1].rgbtBlue)), 2);

        }
    }
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            if (sqrt(new_pixel_rx[i][j] + new_pixel_ry[i][j]) > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sqrt(new_pixel_rx[i][j] + new_pixel_ry[i][j]);
            }
            if (sqrt(new_pixel_gx[i][j] + new_pixel_gy[i][j]) > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sqrt(new_pixel_gx[i][j] + new_pixel_gy[i][j]);
            }
            if (sqrt(new_pixel_bx[i][j] + new_pixel_by[i][j]) > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sqrt(new_pixel_bx[i][j] + new_pixel_by[i][j]);
            }
        }
    }
    return;
}