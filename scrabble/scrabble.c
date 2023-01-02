#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else if (score2 < score1)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int ALPHABET[26];
    for (int m = 0; m < 26; m++)
    {
        ALPHABET[m] = m + 97
    }
    for (int i = 0; i < strlen(word); i++)
    {
        char word_lower[strlen(word)]
        if (isupper(word[i]))
        {
            word_lower[i] = tolower(word[i]);
        }
        else
        {
            word_lower[i] = word[i];
        }
    }

    int score = 0;
    for (int j = 0; j < strlen(word); j++)
    {
        for (int k = 0; k < 26; k++)
        {
            if (word_lower[j] == ALPHABET[k])
            {
                score = score + POINTS[k];
            }
        }
    }
    return score;
}
