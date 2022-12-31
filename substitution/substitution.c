#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    printf("%i\n", argc);
    if (argc == 2)
    {
        printf("Valid\n");
    }
    else if (argc == 0 || argv[2] != NULL)
    {
        printf("%s\n", argv[2]);
        printf("Usage: ./substitution key\n");
    }
    else
    {
        printf("Key must contain 26 characters.\n");
    }
}