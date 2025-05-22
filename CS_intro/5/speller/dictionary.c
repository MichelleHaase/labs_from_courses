// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash function sorts by first two letters so 26*26 buckets
const unsigned int N = 676;
int counter = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // must be case insensitive; only return true if word in dict; no hardcoding common words
    // dict is alphabetically ordered; 1 word per line the /n wont start /w '; only letters and ';
    // at least one word all within LENGHT
    if (word == NULL || strlen(word) == 0)
    {
        return false;
    }
    // changing all letters to lowercase doesnt work, read-only
    // making copy then chaning it
    char *lower_word = malloc((strlen(word) + 1));
    if (lower_word == NULL)
    {
        return false;
    }
    for (int i = 0; i < strlen(word); i++)
    {
        if (word[i] == '\'')
        {
            lower_word[i] = word[i];
        }
        else
        {
            lower_word[i] = tolower(word[i]);
        }
    }
    lower_word[strlen(word)] = '\0';
    // calculate the array index of the hashfunction
    unsigned int hash;
    if (strlen(lower_word) < 2)
    {
        // if the word is a i or some other single letter word, return it to the first bucket of
        // Letter
        hash = (lower_word[0] - 'a') * 26;
    }
    else
    {
        hash = ((lower_word[0] - 'a') * 26) + lower_word[1] - 'a';
    }

    for (node *n = table[hash]; n != NULL; n = n->next)
    {
        // go through all entries in the bucket and check if it fits the word
        if (strcmp(n->word, lower_word) == 0)
        {
            free(lower_word);
            return true;
        }
    }
    free(lower_word);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO? :  Hash function sorts after first and second letter of the alphabet
    //          it substracts 'A' because of ASCII then multiplies the letternumber with 26,
    //          so that the first Bucket Aa is at position 0 and B buckets only start at 27,
    //          then adds the number of the seond letter -> Ab = 1 Ad = 3
    //          no toupper since the dict is all lower compare to 'a' not 'A'
    if (strlen(word) < 2)
    {
        // if the word is a i or some other single letter word, return it to the first bucket of
        // Letter
        return (word[0] - 'a') * 26;
    }
    return ((word[0] - 'a') * 26) + word[1] - 'a';

    /*
        ((word[0] -65) *26) + word[1] -65
        Aa == 0
        Az == 25!
        Ba == 26
        Ca == 52
        Da == 78
        Zz == 675
    */
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // opening Dict
    FILE *dict = fopen(dictionary, "r");
    // exiting if dict is empty
    if (dict == NULL)
    {
        return false;
    }
    // allocating space for words
    char new_word[LENGTH + 1];
    // read in file
    while (fscanf(dict, "%s", new_word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dict);
            return false;
        }
        strcpy(n->word, new_word);
        unsigned int bucket = hash(new_word);
        n->next = table[bucket];
        table[bucket] = n;
        counter++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    // go through all buckets of the table
    for (int i = 0; i < N; i++)
    {
        node *tmp = table[i];

        // go through all contents of current bucket
        while (tmp != NULL)
        {
            // set n to the node before it as long as it isnt NULL
            node *n = tmp->next;
            // free the old node
            free(tmp);
            tmp = n;
        }
    }
    return true;
}
