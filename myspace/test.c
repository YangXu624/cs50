#include <cs50.h>
#include <stdio.h>
#include <string.h>

//To determine if 'a' and 'b' values are stored in a for loop even after the loop repeats

int main(void)
{
    int a = 0;
    int b = 0;
    for (int i = 0; i < 1; i++)
    {
        a = 10;
        b = 20;
        for (int j = 0; j < 5; j++)
        {
            if (0 < 1)
            {
                a = a + 1;
                b = b + 1;
                printf("a is %i, b is %i\n", a, b);
            }
        }
    }
    return 0;
}

//Conclusion: 'a' and 'b' are stored even after 'j' changes and the loop repeats