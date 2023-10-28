#include <stdio.h>
#include <math.h>

char get_filename(int i)
{
    int a = floor(i / 100);
    int b = floor((i - a * 100) / 10);
    int c = i - a * 100 - b * 10;
    int num[3] = {a, b, c};

    char *filename[7] = {'0', '0', '0', '.', 'j', 'p', 'g'};

    return *filename;
}

int main()
{
    int k = get_filename(0);
    printf("%c", k);
}
