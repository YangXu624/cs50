#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argv[2] != NULL)
    {
        printf("Please only input 1 argument\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        return 1;
    }


}
