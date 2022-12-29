#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Collecting a valid input where 0 < height < 9
    int height;
    do
    {
        height = get_int("Height:");
    }
    while (height > 8 || height < 1);

    for (int i = 1; i <= height; i++)
    {
        // Print left side spaces
        for (int k = height; k > i; k--)
        {
            printf(" ");
        }

        // Print left side hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Print centre spaces
        printf("  ");

        // Print right side hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}