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

    long p;
    long q;
    long r;
    long s = 0;
    for (int i = 1; i < 9; i++)
    {
        p = (cn % pw(10,2*i));
        q = p - (p % pw(10,2*i - 1));
        r = q / pw(10,2*i - 1);
        printf("%li", r);
        if (r > 4)
        {
            s = s + r - 9;
        }
        else
        {
            s = s + r;
        }
        printf("%li\n", s);
    }
}