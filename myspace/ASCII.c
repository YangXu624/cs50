#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for (int i = 97; i < 123; i++)
    {
        printf("%c has the ASCII value of %i\n", i, i);
    }
}