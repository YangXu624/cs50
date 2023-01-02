#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2 && strlen(argv[1]) == 26)
    {
        string s = argv[1];
        char ss[26];

        //Filtering out invalid characters in key, and transforming all of the key into lower case for ease of programming
        //Upper case characters will be reverted back to uppercase towards the end of programme
        for (int m = 0; m < 26; m++)
            if (isupper(s[m]))
            {
                ss[m] = tolower(s[m]);
            }
            else if (islower(s[m]))
            {
                ss[m] = s[m];
            }
            else
            {
                printf("Usage: ./substitution key\n");
                return 1;
            }

        //Filtering out duplicate characters in key
        for (int q = 0; q < 26; q++)
        {
            for (int r = 0; r < 26; r++)
            {
                if (ss[q] == ss[r] && r != q)
                {
                    printf("Usage: ./substitution key\n");
                    return 1;
                }
            }
        }

        //Comparing input key with a standard set of alphabet sequences to generate a difference in ASCII value
        string st = "abcdefghijklmnopqrstuvwxyz";
        int diff[26];
        for (int i = 0; i < 26; i++)
        {
            diff[i] = st[i] - ss[i];
        }

        //Conversion of all input characters to lower case for ease of programming
        string in = get_string("plaintext: ");
        char in_lower[strlen(in)];
        for (int p = 0; p < strlen(in); p++)
        {
            if (isupper(in[p]))
            {
                in_lower[p] = tolower(in[p]);
            }
            else
            {
                in_lower[p] = in[p];
            }
        }

        //Generation of cipher text
        printf("ciphertext: ");
        int out[strlen(in)];
        for (int j = 0; j < strlen(in); j++)
        {
            //If the 'j'th character of plain text input is an alphabet, translate it according to key
            if (islower(in[j]) || isupper(in[j]))
            {
                for (int k = 0; k < 26; k++)
                {
                    if (in_lower[j] == st[k])
                    {
                        if (islower(in[j]))
                        {
                            out[j] = st[k] - diff[k];
                            printf("%c", out[j]);
                        }
                        //If originally upper case, revert back to upper case to print out
                        else if (isupper(in[j]))
                        {
                            out[j] = st[k] - diff[k];
                            printf("%c", toupper(out[j]));
                        }
                    }
                }
            }
            //If the 'j'th character of plain text input is not an alphabet, print it as it is
            else
            {
                printf("%c", in[j]);
            }
        }
        printf("\n");
        return 0;
    }

    //Invalid keys
    else if (argc == 0 || argv[2] != NULL)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}