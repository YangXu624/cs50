#include <cs50.h>
#include <stdio.h>

//To compare which format works better to generate ordered pairs (a, b), where a < b
//Two formats differ at line 11 and line 21
int main(void)
{
    //Format 1
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; i < j && j < 5; j++)
        {
            printf("(%i, %i), ", i, j);
        }
    }
    printf("\n");

    //Format 2
    for (int k = 0; k < 5; k++)
    {
        for (int l = k + 1; l < 5; l++)
        {
            printf("(%i, %i), ", k, l);
        }
    }
    printf("\n");
}

//Results: Format 1 did not print out anything, but format 2 printed out perfectly as intended
//Conclusion: Format 2 works, while format 1 does not