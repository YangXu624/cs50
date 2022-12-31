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
                    printf("%c\n", out[j]);
                }
                else
                {
                    printf("%c\n", in[j]);
                }
            }
        }
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