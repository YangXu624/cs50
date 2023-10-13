#include <cs50.h>
#include <stdio.h>

//To find out if integer arrays are set to 0 if not specified
int array[10];

int main(void)
{
    printf("%i\n", array[1]);
}

//Result: Printed 0
//Conclusion: Integer arrays are set to 0 if not specified