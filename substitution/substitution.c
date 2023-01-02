#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2 && strlen(argv[1]) == 26)
    {
        printf("Valid\n");

        string s = argv[1];
        string st = "abcdefghijklmnopqrstuvwxyz";

        int diff[26];

        for (int i = 0; i < 26; i++)
        {
            diff[i] = st[i] - s[i];
        }

        string in = get_string("plaintext: ");
        int out[strlen(in)];

        for (int j = 0; j < strlen(in); j++)
        {
            for (int k = 0; k < 26; k++)
            {
                if (in[j] == st[k])
                {
                    out[j] = st[k] - diff[k];
                    printf("%i%i\n", j, k)
                }
                else
                {
                    out[j] = out[j];
                }
            }
            printf("%c", out[j]);
        }
        printf("\n");
    }
    else if (argc == 0 || argv[2] != NULL)
    {
        printf("Usage: ./substitution key\n");
    }
    else
    {
        printf("Key must contain 26 characters.\n");
    }
}