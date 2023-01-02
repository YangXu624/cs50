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
        string st = "abcdefghijklmnopqrstuvwxyz";
        string stt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        int diff_lower[26];
        int diff_upper[26];

        for (int i = 0; i < 26; i++)
        {
                diff_lower[i] = st[i] - s[i];
                diff_upper[i] = stt[i] - s[i];
        }

        string in = get_string("plaintext: ");
        printf("ciphertext: ");

        int out[strlen(in)];

        for (int j = 0; j < strlen(in); j++)
        {
            //If the 'j'th character is an alphabet, regardless of case
            if (((64 < in[j] && in[j] < 91) || (96 < in[j] && in[j] < 123)))
            {
                for (int k = 0; k < 26; k++)
                {
                    if (in[j] == st[k])
                    {
                        out[j] = st[k] - diff_lower[k];
                        printf("%c", out[j]);
                    }
                    else if (in[j] == stt[k])
                    {
                        out[j] = stt[k] - diff_upper[k];
                        printf("%c", out[j]);
                    }
                }
            }
            else
            {
                printf("%c", in[j]);
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