#include <cs50.h>
#include <stdio.h>

long pw(long a, long b)
{
    long c = 1;
    for (int i = 0; i < b; i++)
    {
        c = c * a;
    }
    return(c);
}

int main (void)
{
    //Ask for input of credit card number
    long cn = get_long ("Number:");

    int k = 0;
    for (int i = 0; i < 9; i++)
    {
        k = k + (cn - (cn % pw(10, 2*i)))/pw(10, 2*i);
        printf("%i\n", k);
    }
    printf("%i\n", k);
}