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

    //Even-positioned digits first
    for (int i = 1; i < 9; i++)
    {
        //p represents an integer with k digits, we will vary k to cover all even-positioned digits
        p = (cn % pw(10,2*i));

        //By subtracting the rightmost k-1 digits, we obtain q, which has the same 'k'th digit as p, followed by a chain of k-1 '0's
        q = p - (p % pw(10,2*i - 1));

        //By dividing with an appropriate power of 10, we can obtain the specific 'k'th digit as a single digit number
        r = q / pw(10,2*i - 1);

        //Processing of the sum of the sum of double the even-positioned digits. Note that if r is an integer between 0 and 4 inclusive,
        //double of r would still be single-digit, meaning that the sum of digits of 2r would be equal to 2r
        if (r > 4)
        {
            s = s + 2*r - 9;
        }
        else
        {
            s = s + 2*r;
        }

        //Print to check
        printf("%li\n", s);
    }

    long t=0;
    //Odd-positioned digits
    for (int i = 1; i < 9; i++)
    {
        //p represents an integer with k digits, we will vary k to cover all odd-positioned digits
        p = (cn % pw(10,2*i - 1));

        //By subtracting the rightmost k-1 digits, we obtain q, which has the same 'k'th digit as p, followed by a chain of k-1 '0's
        q = p - (p % pw(10,2*i - 2));

        //By dividing with an appropriate power of 10, we can obtain the specific 'k'th digit as a single digit number
        r = q / pw(10,2*i - 2);

        //Print to check
        printf("%li", r);

        //Summing up of odd-positioned digits
        t = t + r;

        //Print to check
        printf(", %li\n", t);
    }

    //Add the even-digits part and the odd-digits part together
    long u = s + t;

    printf("**%li\n", u);

    long v = u % 10;
    printf("**%li\n", v);

    if (v == 0)
    {
        if (4 <= cn/pw(10,12) && cn/pw(10,12) < 5)
        {
            printf("VISA\n");
        }

        else if ((34 <= cn/pw(10,13) && cn/pw(10,13) < 35) || (37 <= cn/pw(10,13) && cn/pw(10,13) < 38))
        {
            printf("AMEX\n");
        }

        else if (4 <= cn/pw(10,15) && cn/pw(10,15) < 5)
        {
            printf("VISA\n");
        }

        else if (51 <= cn/pw(10,14) && cn/pw(10,14) < 56)
        {
            printf("MASTERCARD\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }
}