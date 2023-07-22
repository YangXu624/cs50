#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    RGBTRIPLE pixel = image[0][0];
    pixel.rgbtBlue = 0x1f;
    pixel.rgbtRed = 0xff;
    pixel.rgbtGreen = 0xff;
}
