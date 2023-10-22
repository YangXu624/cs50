#include <stdio.h>

void change(int *n)
{
    *n = 40 + *n;
}

int main()
{
    int a = 50;
    int *p = &a;

    change(&a);

    printf("%i\n", *p);
}