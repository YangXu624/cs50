#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a = get_int ("a: ");
    int b = get_int ("b: ");
    int c = 1;
    for (int i = 0; i < b; i++)
    {
        c = c * a;
    }
    printf("%i\n", c);
}