#include <cs50.h>
#include <stdio.h>

float count_letters(string tx);
float count_words(string tx);
float count_sentences(string tx);

int main(void)
{
    string tx = get_string("Text: ");

    float x = (count_letters(tx)/count_words(tx)) * 100.0;
    float y = (count_sentences(tx)/count_words(tx)) * 100.0;
    //Pre-processed index
    float index1 = 0.0588 * x - 0.296 * y - 15.8;
    //Rounding up of index if it is .5 or more, instead of blindly taking floor function
    int index = index1 + 0.5;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

float count_letters(string tx)
{
    int i = 0;
    float c = 0;
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
        //Proceed to next character
        i = i + 1;
    }
    //Repeat until the end of the entire string
    while (tx[i] != '\0');
    return c;
}

float count_words(string tx)
{
    int j = 0;
    float s = 0;
    do
    {
        //If the 'j'th character is a space, add 1 to counter 's'
        //Note: We do this because (number of words = number of spaces + 1)
        if (tx[j] == 32)
        {
            s = s + 1;
        }
        else
        {
            s = s + 0;
        }
        //Proceed to next character
        j = j + 1;
    }
    while (tx[j] != '\0');
    //Accounting for + 1, since there will be one more word than there are spaces
    s = s + 1;
    return s;
}

float count_sentences(string tx)
{
    int k = 0;
    float t = 0;
    do
    {
        //If the 'k'th character is a '.', '!', or '?', add 1 to counter 'k'
        //Note that (number of above punctation = number of sentences)
        if (tx[k] == 46 || tx[k] == 33 || tx[k] == 63)
        {
            t = t + 1;
        }
        else
        {
            t = t + 0;
        }
        //Proceed to next character
        k = k + 1;
    }
    while (tx[k] != '\0');

    return t;
}