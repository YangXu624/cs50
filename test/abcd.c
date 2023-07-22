#include <cs50.h>
#include <stdio.h>

int score[9][9];
int candidate_count = 9;
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[9];
pair pairs[9 * (9 - 1) / 2];

int main(void)
{
    // TODO
    int counter = 0;
    do
    {
        int highest = 0;
        for (int i = 0; i < candidate_count; i++)
        {
            for (int j = i + 1; j < candidate_count; j++)
            {
                if (score[i][j] > highest)
                {
                    highest = score[i][j];
                    pairs[counter].winner = i;
                    pairs[counter].loser = j;
                }
                else if (score[j][i] > highest)
                {
                    highest = score[j][i];
                    pairs[counter].winner = j;
                    pairs[counter].loser = i;
                }
            }
        }
        score[pairs[counter].winner][pairs[counter].loser] = 0;
        counter++;
        printf("%i\n", counter);
    }
    while (counter < 10);
    return 0;
}