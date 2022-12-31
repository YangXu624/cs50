#include <cs50.h>
#include <stdio.h>

int count_letters(string tx);
int count_words(string tx);

int main(void)
{
    string tx = get_string("Text: ");
    printf("%i\n", count_letters(tx));
    printf("%i\n", count_words(tx));
}

int count_letters(string tx)
{
    int i = 0;
    int c = 0;
    do
    {
        //If the 'i'th character is an alphabet, add 1 to counter 'c'
        if ((64 < tx[i] && tx[i] < 91) || (96 < tx[i] && tx[i] < 123))
        {
            c = c + 1;
        }
        //If the 'i'th character is not an alphabet, counter 'c' remains constant
        else
        {
            c = c + 0;
        }
        i = i + 1;
    }
    //Repeat until the end of the entire string
    while (tx[i] != '\0');
    return c;
}

int count_words(string tx)
{
    int s = 0;
    int j = 0;
    do
    {
        //If the 'j'th character is a space, add 1 to counter 's'
        //Note: We do this because (number of words = number of spaces + 1)
        if(tx[j] == 32)
        {
            s = s + 1;
        }
        else
        {
            s = s + 0;
        }
    }
    while (tx[j] != '\0');
    //Accounting for + 1, since there will be one more word than there are spaces
    s = s + 1;
    return s;
}