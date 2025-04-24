/* input is a amount of money in cents the smallest amount of coins should be returned
optiona are 25 10 5 1 cent; if statements in while loop as long as != 0 one counter for
all if statements and each statement substracts their amount and increments the counter*/
#include <cs50.h>
#include <stdio.h>

int counter = 0;
int amount = 0;

int main(void)
{
    do
    {
        amount = get_int("Change owed ");
        // gets the Change from the user
    }
    while (amount < 0);
    // repromts as long as the input is not a positive number

    while (amount > 0)
    // goes thrue if else till amount is 0
    {
        if (amount >= 25)
        {
            amount = amount - 25;
            counter++;
        }
        else if (amount >= 10)
        {
            amount = amount - 10;
            counter++;
        }
        else if (amount >= 5)
        {
            amount = amount - 5;
            counter++;
        }
        else if (amount >= 1)
        {
            amount = amount - 1;
            counter++;
        }
    }

    printf("%i\n", counter);
    // prints the overall number of coins
}
