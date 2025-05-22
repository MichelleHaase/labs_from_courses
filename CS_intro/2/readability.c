#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int get_wordcount(string text);
double get_letters(string text, int wordcount);
double get_sentences(string text, int wordcount);
int coleman_liau(double l, double s);

/* L= avrg num of letters, not chars per 100 words
    s= num of scentences per 100 words
        index = 0.0588 * L - 0296 * S - 15.8*/
int main(void)
{
    string text = get_string("Text: ");
    int wordcount = get_wordcount(text);
    double letters_per_100 = get_letters(text, wordcount);
    double senctencves_per_100 = get_sentences(text, wordcount);
    int index = coleman_liau(letters_per_100, senctencves_per_100);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
/*
< 1before grade 1
>16 grade 16+
*/
int coleman_liau(double l, double s)
{
    double index = 0.0588 * l - 0.296 * s - 15.8;
    int index2 = round(index);
    return index2;
}

int get_wordcount(string text)
{
    int wordcount = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isspace(text[i]) != 0)
            wordcount++;
    }
    // printf("wordcount: %i\n", wordcount);
    return wordcount;
}

double get_letters(string text, int wordcount)
{
    double lettercount = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            lettercount++;
        }
    }
    // printf("lettercount: %f\n", lettercount);
    lettercount = lettercount / wordcount * 100;
    return lettercount;
}

double get_sentences(string text, int wordcount)
{
    double sentencecount = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (strchr("?.!", text[i]) != NULL)
        {
            sentencecount++;
        }
    }
    sentencecount = sentencecount / wordcount * 100;
    // printf("sentencecount: %i\n", sentencecount);
    return sentencecount;
}
