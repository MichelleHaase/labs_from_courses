/*
anyone gets 50% of first choice winns directly
if not the candidate with fewest votes is eliminated (completly from all levels) and their votes are
now the second choice so same loop as finding highest votes then if choices[0]== Lowest count
choices[1] then repeat tiil 50%
*/

#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // if if (strcmp(candidates[i].name, name) == 0)
    // inside preferences array so for i in voter_count and j in candidate count
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // for in in candidate_count fot j in voter ocunt if candidates[i].eliminated = false
    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (candidates[preferences[i][j]].eliminated == false)
            {
                candidates[preferences[i][j]].votes++;
                break;
            }
        }
    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    int counter = 0;
    int half_the_votes = round(voter_count / 2);
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > half_the_votes)
        {
            printf("%s\n", candidates[i].name);
            // return true;
            counter++;
        }
    }
    if (counter > 0)
    {
        return true;
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // find the candidate that has the lowest votes and is still valid
    // setting lowest count to the highest possible number so it can be overwritten with lower vote counts
    int lowest_count = voter_count;
    for (int i = 0; i < candidate_count; i++)
    {
        // overwriting lowest_count if the next Value is lower
        if (lowest_count > candidates[i].votes && candidates[i].eliminated == false)
        {
            lowest_count = candidates[i].votes;
        }
    }
    return lowest_count;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // checking if the smallest Vote count calculated in find_min() is the same for all candidates
    // ergo a total Tie
    int valid_candidates = 0;
    int counter = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        // counting the candidates still in the race
        if (candidates[i].eliminated == false)
        {
            valid_candidates++;
        }
        // checking if valid candidates have a vote count equal to min
        if (candidates[i].votes == min && candidates[i].eliminated == false)
        {
            counter++;
        }
    }
    // checking if the amount of candidates with a voter count of min is equal to the num of valid candidates
    if (counter == valid_candidates)
    {
        return true;
    }
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // set .eliminate True for everyone with votecount min
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    return;
}
