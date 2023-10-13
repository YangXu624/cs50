#include <stdio.h>
#include <cs50.h>

typedef struct
{
    int num1;
    int num2;
} t;

int main(void)
{
    t array[5][3];
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            array[i][j].num1 = j + 3 * i;
            array[i][j].num2 = array[i][j].num1 + 100;
            printf("%i, %i, ", array[i][j].num1, array[i][j].num2);
        }
    }

    printf("\n");

    int *p = &array[0][0].num1;

    for (int i = 0; i < 30; i++)
    {
        printf("%i, ", *(p+i));
    }

    printf("\n");
}