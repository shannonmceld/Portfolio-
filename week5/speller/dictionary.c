// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

//global word counter
int flag = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = (46 * 'z');

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //hash word to obtain hash value
    int index = hash(word);
    //access linked list at index in hash table
    node *cursor = table[index];
    //traverse linked list
    while (cursor != NULL)
    {
        //look for case-insensitive word
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        // move to the next word
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int hash = 0;
    int i = 0;
    int n = strlen(word);
    //used hash function from hash table prectice video by DOUG LLOYD
    for (i = 0; i < n; i++)
    {
        // change all letter of word to lower case
        hash += tolower(word[i]);
    }
    // return hash value within hash bucket limit
    return (hash % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //open dictionary file
    FILE *file = fopen(dictionary, "r");
    // file cannot be open return function false
    if (file == NULL)
    {
        return false;
    }
    // character array
    char word_array[LENGTH + 1];
    // read string from file
    while (fscanf(file, "%s", word_array) != EOF)
    {
        // create a new node for each word
        node *new_node = malloc(sizeof(node));
        // return function if NULL
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        //copy word in new node
        strcpy(new_node->word, word_array);
        //hash word to obtain an hash value
        int index = hash(new_node->word);
        node *head = table[index];

        //  insert node into hash table
        new_node-> next = table[index];
        table[index] = new_node;
        flag++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return flag;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        //free up allocated memory
        node *head = table[i];
        //create two variable to point at head pointer
        node *cursor = head;
        node *tmp = head;

        while (cursor != NULL)
        {
            //use one variable to move through the list
            cursor = cursor->next;
            // while we free the list
            free(tmp);
            tmp = cursor;
        }

    }

    return true;
}
