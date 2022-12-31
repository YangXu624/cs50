#include <cs50.h>
#include <stdio.h>

int count_letters(string tx)
{
    do
    {
        int i = 0;
        int c = 0;
        if ((64 < tx[i] && tx[i] < 91) || (96 < tx[i] && tx[i] < 123))
        {
            c = c + 1
        }
        else
        {
            c = c
        }
        i = i + 1
    }
    while tx[i] != '0\'
}

int main(void)
{
    string tx = get_string("Text: ");

}