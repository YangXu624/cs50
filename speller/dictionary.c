// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

int count;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * LENGTH;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *ptr = table[hash(word)];

    while (ptr != NULL)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    };
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; i < LENGTH + 1; i++)
    {
        if (word[i] == '\0')
        {
            break;
        }
        sum += tolower(word[i]) - 97;
    }
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Please input a dictionary!\n");
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != NULL)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Insufficient memory to allocate for loading.\n");
            return false;
        }

        n->next = table[hash(n->word)];
        table[hash(n->word)] = n;
        count++;
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *tmp = ptr;
            ptr = ptr->next;
            free(tmp);
        };
        table[i] = NULL;
    }
    return true;
}
