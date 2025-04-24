#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        // if vote of name returns false
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    // validate that the name is equal account for capitilisation?
    // for i in array candidate count ;if candidate[i].name == name - candidate[i].vote += 1 return
    // True
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // void means this should be possible with only access to global vars
    // candatites with most votes assign first entry to array then check if next bigger, for len of
    // array

    // setting first entry as highest value
    int voter_count = 0;
    // adding up how many votes each candidate got
    for (int i = 0; i < candidate_count; i++)
    {
        voter_count = voter_count + candidates[i].votes;
    }
    int highest_count = candidates[0].votes;
    for (int i = 0; i < voter_count; i++)
    {
        // overwriting highest_count if the next Value is higher
        if (highest_count < candidates[i].votes)
        {
            highest_count = candidates[i].votes;
        }
    }
    // creating an Array with len of max candiates
    string list_winners[MAX];
    int index_list = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        // population array with all winners
        if (highest_count == candidates[i].votes)
        {
            printf("%s\n", candidates[i].name);
            // list_winners[index_list] = candidates[i].name;
            // index_list++;
        }
    }
    return;
}
