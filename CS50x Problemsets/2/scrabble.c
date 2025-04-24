#include <cs50.h>
#include <stdio.h>
#include <string.h>

int calc_points(string word);

int main(void)
{
    // get the inputs from Users to compare
    string guess_1 = get_string("Player 1: ");
    string guess_2 = get_string("Player 2: ");
    // calls calulate points to get the points for each word
    int points_p1 = calc_points(guess_1);
    int points_p2 = calc_points(guess_2);
    // decides who won or if it's a Tie
    if (points_p1 > points_p2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points_p1 < points_p2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int calc_points(string word) // takes the Unser input from main as argument
{
    int points = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    // loops till i adds up to the words length
    {
        /* checks if the current char of the word in the loop, is in
        one of the strings set as "haystack" to look thru and adds points accordingly */
        if (strchr("aeilnorstuAEILNORSTU", word[i]) != NULL)
        {
            points++;
        }
        else if (strchr("dgDG", word[i]) != NULL)
        {
            points = points + 2;
        }
        else if (strchr("bcmpBCMP", word[i]) != NULL)
        {
            points = points + 3;
        }
        else if (strchr("fhvwyFHVWY", word[i]) != NULL)
        {
            points = points + 4;
        }
        else if (strchr("kK", word[i]) != NULL)
        {
            points = points + 5;
        }
        else if (strchr("jxJX", word[i]) != NULL)
        {
            points = points + 8;
        }
        else if (strchr("qzQZ", word[i]) != NULL)
        {
            points = points + 10;
        }
    }
    return points; // returns the added up points
}
