#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2 && strlen(argv[1]) == 26)
    {
        printf("Valid\n");

        string s = argv[1];
        char ss[26];
        for (int m = 0; m < 26; m++)
            if (isupper(s[m]))
            {
                ss[m] = tolower(s[m]);
            }
            else
            {
                ss[m] = s[m];
            }

        string st = "abcdefghijklmnopqrstuvwxyz";

        int diff[26];

        for (int i = 0; i < 26; i++)
        {
                diff[i] = st[i] - ss[i];
        }

        string in = get_string("plaintext: ");
        printf("ciphertext: ");

        int out[strlen(in)];

        for (int j = 0; j < strlen(in); j++)
        {
            for (int k = 0; k < 26; k++)
            {
                if (in[j] == st[k])
                {
                    if (islower(in[j]))
                    {
                        out[j] = st[k] - diff[k];
                        printf("%c", out[j]);
                    }
                    else if (isupper(in[j]))
                    {
                        out[j] = st[k] - diff[k];
                        printf("%c", isupper(out[j]));
                    }
                }
            }
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