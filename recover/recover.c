#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argv[2] != NULL)
    {
        printf("Please only input 1 argument\n");
        return 1;
    }

    FILE *in_file = fopen(argv[1], "r");

    if (in_file == NULL)
    {
        return 1;
    }

    unsigned char buffer[BLOCK_SIZE];
    FILE *out_file = NULL;
    char *filename = malloc(8 * sizeof(char));
    int count = 0;
    while (fread(buffer, sizeof(char), BLOCK_SIZE, in_file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] > 0xdf && buffer[3] < 0xf0)
        {
            if (count > 0)
            {
                fclose(out_file);
            }

            sprintf(filename, "%03i.jpg", count);

            out_file = fopen(filename, "w");

            count++;
        }
        if (out_file != NULL)
        {
            fwrite(buffer, sizeof(char), BLOCK_SIZE, out_file);
        }
    }
    fclose(out_file);
    free(filename);
    fclose(in_file);
}
