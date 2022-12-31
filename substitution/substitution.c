#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 26)
    {
        printf("Valid\n");
    }
    else if (argc == 0 || for (int i = 0; i < 26; i++){argv[i] < 65})
    {
        printf("Usage: ./substitution key\n");
    }
    else
    {
        printf("Key must contain 26 characters.\n");
    }
}