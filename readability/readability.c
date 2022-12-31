#include <cs50.h>
#include <stdio.h>

int count_letters(string tx)
{
    do
    {
        int i = 0;
        if ((64 < tx[i] && tx[i] < 91) || (96 < tx[i] && tx[i] < 123))
        {
            i = i + 1
        }
    }
    while tx[i] != '0\'
}

int main(void)
{
    string tx = get_string("Text: ");

}