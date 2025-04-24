#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 0;
    // declared outside of Loop so other functions can use it
    do
    {
        n = get_int("How high should it be? ");
        // lets user define hight of pyramid
    }
    while (n <= 0 || n >= 9);
    // condition for the number to be between 1 and 8 incl

    for (int i = 1; i <= n; i++)
    // defines the number of rows
    {
        for (int spaces = i; spaces < n; spaces++)
        // gives the number of Spaces for each line
        {
            printf(" ");
        }
        for (int hashes = n - i; hashes < n; hashes++)
        // prints the left Pyramid
        {
            printf("#");
        }
        printf("  ");
        // seperator between pyramids
        for (int hashes_right = n - i; hashes_right < n; hashes_right++)
        // prints the right pyramid
        {
            printf("#");
        }
        printf("\n");
        // line break after each finished line
    }
}
