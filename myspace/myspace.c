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
            printf("%i, ", array[i][j].num1);
        }
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            array[i][j].num2 = array[i][j].num1 + 100;
            printf("%i, ", array[i][j].num2);
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

// Conclusion:
// 1. Consecutive arrays are stored in consecutive addresses, for example array[0], array[1], array[2] and so on...
// 2. For 2D arrays and similarly arrays of higher dimensions, array[i][j][0], array[i][j][1], array[i][j][2], ...
// array[i][j + 1][0], array[i][j + 1][1], array[i][j + 1][2], ... In such a way that the rightmost dimension is the first to change
// 3. For arrays with more than 1 variable type, for example array[k].num1 and array[k].num2, the values of array[k] are all stored
// before the values of array[k + 1] is stored, i.e. array[k].num2 is stored before array[k + 1].num1