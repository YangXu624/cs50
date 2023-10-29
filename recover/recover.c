#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cs50.h>

#define BLOCK_SIZE 512

string get_filename(int k);

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
    int count = 0;
    while (fread(buffer, 1, BLOCK_SIZE, in_file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] > 0xdf && buffer[3] < 0xf0)
        {
            string filename = get_filename(count);
            printf("%s\n", filename);

            FILE *out_file = fopen(filename, "a");

            fwrite(buffer, 1, BLOCK_SIZE, out_file)

            fclose(out_file);

            count++;
        }

    }
    fclose(in_file);

}

string get_filename(int k)
{
    int a = floor(k / 100);
    int b = floor((k - a * 100) / 10);
    int c = k - a * 100 - b * 10;

    string filename = malloc(8 * sizeof(char));
    sprintf(filename, "%i%i%i.jpg", a, b, c);

    return filename;
}
