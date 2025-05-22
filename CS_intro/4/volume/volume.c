// Modifies the volume of an audio file

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;
typedef int16_t two_byte;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);
    int counter = 0;
    two_byte chunk, chunk2;
    // int counter2 = 0;
    while (fread(&chunk, sizeof(two_byte), 1, input) != 0)
    {
        if (counter < (HEADER_SIZE / 2)) // half the header size since it's two chunk bits
        {
            fwrite(&chunk, sizeof(two_byte), 1, output);
            counter++;
            // printf("%i\n", chunk);
        }
        else
        {
            // chunk2 = chunk;
            chunk *= factor;
            fwrite(&chunk, sizeof(two_byte), 1, output);
            // counter2 ++;
        }
    }
    // printf("%i\n%i\n", chunk, chunk2);

    // TODO: Copy header from input file to output file
    // 1 byte for 44 times
    // TODO: Read samples from input file and write updated data to output file

    // Close files
    fclose(input);
    fclose(output);
}
