#include <cs50.h>
#include <stdio.h>

int main (void)
{
    //Ask for input of credit card number
    long c = get_long ("Number:");

    for (int i = 0; i < 9; i++)
    {
        float a = (c - (c % pow(10,(16 - 2*i))))/pow(10, 2 * i)
        printf("%f\n", a);
    }
}