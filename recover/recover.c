#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE = 512

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

    unsigned int buffer[BLOCK_SIZE];
    while (fread(buffer, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] > 0xdf && buffer[3] < 0xf0)
        {
            FILE *f1 = fopen("000.jpg", "a");
            for (int i = 0; i < BLOCK_SIZE; i++)
            {
                fprintf(000.jpg, "%i ", buffer[i]);
            }
        }

    }

}
