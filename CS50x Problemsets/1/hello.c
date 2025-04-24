#include <cs50.h>
#include <stdio.h>
// CS50 Lib for get_string

int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
