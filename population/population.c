#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int p;
    int e;
    do
    {
        p = get_int("Start size: ");
    }
    while (p < 9);
    // TODO: Prompt for end size
    do
    {
        e = get_int("End size: ");
    }
    while (e < p);
    // TODO: Calculate number of years until we reach threshold
    int c = -1;
    for (int i = p; i <= e;)
    {
        i = i + (float) (i / 3) - (float) (i / 4);
        c = c + 1;
    }
    // TODO: Print number of years
    printf("Years: %i\n", c);
}
