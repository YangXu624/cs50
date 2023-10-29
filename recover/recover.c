#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cs50.h>

#define BLOCK_SIZE 512

char get_filename(int k);

int main(int argc, char *argv[])
{
    if (argv[2] != NULL)
    {
        printf("Please only input 1 argument\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        return 1;
    }

    int buffer[BLOCK_SIZE];
    int count = 0;
    printf("%i\n", count);
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        printf("%i\n", buffer[3]);
        return 1;
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] > 0xdf && buffer[3] < 0xf0)
        {
            char filename = get_filename(k);
            FILE *file1 = fopen(&filename, "a");
            for (int i = 0; i < BLOCK_SIZE; i++)
            {
                fprintf(file1, "%i ", buffer[i]);
            }
            count++;
        }

    }

}

char get_filename(int k)
{
    int a = floor(k / 100);
    int b = floor((k - a * 100) / 10);
    int c = k - a * 100 - b * 10;

    string filename = NULL;
    sprintf(filename, "%i%i%i.jpg", a, b, c);

    return *filename;
}
