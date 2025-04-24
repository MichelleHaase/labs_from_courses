#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t fivehundred_twelve_bytes[512];
// typedef uint16_t fivehundred_twelve_bytes2[512];

int main(int argc, char *argv[])
{
    // check if filenaame is given; no further tests since i don't know the constraints of the input
    // files
    if (argc != 2)
    {
        printf("Usage: ./recover FILENAME\n");
        return 1;
    }
    // opening the file with the data to recover
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("unable to process File\n");
        return 2;
    }

    // reading 512 byte chunks till there are no more in the file
    fivehundred_twelve_bytes buffer_512;
    int first = 0; // setting counter so the first conditonal only starts once
    char *filename = malloc(8 * sizeof(char));
    int filename_counter = 0;
    FILE *img = NULL;

    while (fread(&buffer_512, sizeof(fivehundred_twelve_bytes), 1, infile) != 0)
    {
        if (buffer_512[0] == 0xff && buffer_512[1] == 0xd8 && buffer_512[2] == 0xff &&
            (buffer_512[3] & 0xf0) == 0xe0 && first == 0)
        {
            first++;
            sprintf(filename, "%03i.jpg", filename_counter);
            // printf("%s\n", filename);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Invalid jpg name: %s\n", filename);
                free(filename);
                fclose(infile);
                return 3;
            }
            fwrite(&buffer_512, sizeof(fivehundred_twelve_bytes), 1, img);
            filename_counter++;
        }
        else if (buffer_512[0] == 0xff && buffer_512[1] == 0xd8 && buffer_512[2] == 0xff &&
                 (buffer_512[3] & 0xf0) == 0xe0 && first != 0)
        {
            fclose(img);
            sprintf(filename, "%03i.jpg", filename_counter);
            img = fopen(filename, "w");
            fwrite(&buffer_512, sizeof(fivehundred_twelve_bytes), 1, img);
            filename_counter++;
        }

        else if (first != 0)
        {
            fwrite(&buffer_512, sizeof(fivehundred_twelve_bytes), 1, img);
        }
    }
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(infile);
    free(filename);
    return 0;
    // for len of file(argc) go thru 1 byte at a time till header: 0xff, 0xd8, 0xeff 0xe[1-9,a-f]
    // the write header 512 bytes blocks till header again fread; buffer 512 bytes then check if
    // buffe[0-3] match header buffer[3] & 0xf0) == 0xe0 filenames 000.jpg and counting
    // sprintf(filename, "&03i.jpg", 2); - prints to string 03 means int with 3 digits, two is
    // counter FILE *img = fopen(filename, "w"); 512!; fwrite data, size, 512, outpointer file
    // lenght fread !=0
}
