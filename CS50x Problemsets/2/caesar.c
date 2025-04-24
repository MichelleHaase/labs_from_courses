/* cipher
1. get key: amount to shift letters (int)
2. get text to encode
3. encipher text how to wrap round? needs to work for case ignore sonderzeicehn and whitespace and
nums== isalpha
4. print result

1. take key as command line arg  argv are strings check amount of input and that argv[1] is int
(atoi; stdlib.h), exit error 1 too many/little args "Usage: ./caesar key"* error two not int same
message/
2. get text
3. encipher for is alpha islower / is upper in text shift by key, prerserve case A(65) - Z(90),
a(97) - z(122) char c = "A" + 1 == B; looping round ci= (pi + k) % 26 ci == result[i], pi== text[i],
k== key, moodulo 26; convert ASCII to alphabet index A=0 B=1(-65 or 97 for lower) shift with
formular, convert back to ascii
*/

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string encipher(int key, string text);

int main(int argc, string argv[])
{
    int key;
    if (argc == 2 && atoi(argv[1]))
    // if there are two arguments in argv - program name and key and if key can be converted to int
    {
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        key = atoi(argv[1]);
        // set key if conditions are met
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
        // exit and return instructuions if conditions are not met
    }
    string cleartext = get_string("plaintext: ");
    // get text to be enciphered
    string encripted_text = encipher(key, cleartext);
    printf("ciphertext: %s\n", encripted_text);
    // print result
}

string encipher(int key, string text)
{
    for (int i = 0, len = strlen(text); i < len; i++)
    // for as long as the text has letters
    {
        if (isalpha(text[i]) != 0)
        // checking if char is a letter
        {
            if (islower(text[i]) != 0)
            // checking if its lower case
            {
                // looping round ci= (pi + k) % 26 ci == result[i], pi== text[i], k== key, moodulo
                // 26; convert ASCII to alphabet index A=0 B=1(-65 or 97 for lower) shift with
                // formular, convert back to ascii
                //  case A(65) - Z(90), a(97) - z(122) char c = "A" + 1 == B;
                text[i] = (((text[i] - 97) + key) % 26) + 97;
                // override letter;  -97 so a = 0; + 97 to have the right Ascii number
            }
            else
            // check if its uppercase, since it cant be anything else at that point
            {
                text[i] = (((text[i] - 65) + key) % 26) + 65;
                // overwirte upercase letter -65 so A =0; + 65 to have the right Ascii num
            }
        }
    }
    return text;
}
