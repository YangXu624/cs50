#include <stdio.h>

void fn(int arr[]);

int main(){
    int arr[5] = {1, 3, 6, 12, 15};
    fn(&arr[0]);
}

void fn(int arr[])
{
    for (int i = 0; i < 5; i++)
    {
        printf("%i\n", arr[i]);
    }
}