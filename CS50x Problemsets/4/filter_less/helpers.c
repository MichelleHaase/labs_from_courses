#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // all 0 black  all 255 white all values same greys set all to mean?
    // for each row for each collumn mean= mean of RGB RGB = pixels round!
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int mean = round(((float) image[i][j].rgbtBlue + (float) image[i][j].rgbtGreen +
                              (float) image[i][j].rgbtRed) /
                             3);
            image[i][j].rgbtBlue = mean;
            image[i][j].rgbtGreen = mean;
            image[i][j].rgbtRed = mean;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // sepia formular :
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int new_red = round((image[i][j].rgbtRed * 0.393 + image[i][j].rgbtGreen * 0.769 +
                                 image[i][j].rgbtBlue * 0.189));
            int new_green = round((image[i][j].rgbtRed * 0.349 + image[i][j].rgbtGreen * 0.686 +
                                   image[i][j].rgbtBlue * 0.168));
            int new_blue = round((image[i][j].rgbtRed * 0.272 + image[i][j].rgbtGreen * 0.534 +
                                  image[i][j].rgbtBlue * 0.131));

            if (new_red > 255)
            {
                new_red = 255;
            }

            if (new_green > 255)
            {
                new_green = 255;
            }

            if (new_blue > 255)
            {
                new_blue = 255;
            }

            image[i][j].rgbtRed = new_red;
            image[i][j].rgbtGreen = new_green;
            image[i][j].rgbtBlue = new_blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // for i in height ; j minus width
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE image_copy = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = image_copy;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // box blur avr of nine pixels arond for each r g b or less if corner/ edge
    // copy to not over correct on already coreccted values
    RGBTRIPLE i_c[height][width]; // image copy
    int new_red;
    int new_green;
    int new_blue;

    // changeing the middle pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            i_c[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // chaning the middle pixels
            if (i > 0 && i < (height - 1) && j > 0 && j < (width - 1))
            {
                // avarage over the pixel and its 8 adjacent pixels
                new_red = round(((float) i_c[i - 1][j].rgbtRed + i_c[i - 1][j + 1].rgbtRed +
                                 i_c[i - 1][j - 1].rgbtRed + i_c[i][j + 1].rgbtRed +
                                 i_c[i][j - 1].rgbtRed + i_c[i + 1][j].rgbtRed +
                                 i_c[i + 1][j + 1].rgbtRed + i_c[i + 1][j - 1].rgbtRed +
                                 i_c[i][j].rgbtRed) /
                                9.0);
                new_green = round(((float) i_c[i - 1][j].rgbtGreen + i_c[i - 1][j + 1].rgbtGreen +
                                   i_c[i - 1][j - 1].rgbtGreen + i_c[i][j + 1].rgbtGreen +
                                   i_c[i][j - 1].rgbtGreen + i_c[i + 1][j].rgbtGreen +
                                   i_c[i + 1][j + 1].rgbtGreen + i_c[i + 1][j - 1].rgbtGreen +
                                   i_c[i][j].rgbtGreen) /
                                  9.0);
                new_blue = round(((float) i_c[i - 1][j].rgbtBlue + i_c[i - 1][j + 1].rgbtBlue +
                                  i_c[i - 1][j - 1].rgbtBlue + i_c[i][j + 1].rgbtBlue +
                                  i_c[i][j - 1].rgbtBlue + i_c[i + 1][j].rgbtBlue +
                                  i_c[i + 1][j + 1].rgbtBlue + i_c[i + 1][j - 1].rgbtBlue +
                                  i_c[i][j].rgbtBlue) /
                                 9.0);
            }
            // changeing the right edge
            if (i > 0 && i < (height - 1) && j == (width - 1))
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i - 1][j].rgbtRed +
                                 i_c[i - 1][j - 1].rgbtRed + i_c[i][j - 1].rgbtRed +
                                 i_c[i + 1][j].rgbtRed + i_c[i + 1][j - 1].rgbtRed) /
                                6.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i - 1][j].rgbtGreen +
                                   i_c[i - 1][j - 1].rgbtGreen + i_c[i][j - 1].rgbtGreen +
                                   i_c[i + 1][j].rgbtGreen + i_c[i + 1][j - 1].rgbtGreen) /
                                  6.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i - 1][j].rgbtBlue +
                                  i_c[i - 1][j - 1].rgbtBlue + i_c[i][j - 1].rgbtBlue +
                                  i_c[i + 1][j].rgbtBlue + i_c[i + 1][j - 1].rgbtBlue) /
                                 6.0);
            }
            // changeing left edge
            if (i > 0 && i < (height - 1) && j == 0)
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i - 1][j].rgbtRed +
                                 i_c[i - 1][j + 1].rgbtRed + i_c[i][j + 1].rgbtRed +
                                 i_c[i + 1][j].rgbtRed + i_c[i + 1][j + 1].rgbtRed) /
                                6.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i - 1][j].rgbtGreen +
                                   i_c[i - 1][j + 1].rgbtGreen + i_c[i][j + 1].rgbtGreen +
                                   i_c[i + 1][j].rgbtGreen + i_c[i + 1][j + 1].rgbtGreen) /
                                  6.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i - 1][j].rgbtBlue +
                                  i_c[i - 1][j + 1].rgbtBlue + i_c[i][j + 1].rgbtBlue +
                                  i_c[i + 1][j].rgbtBlue + i_c[i + 1][j + 1].rgbtBlue) /
                                 6.0);
            }
            // change upper edge
            if (i == 0 && j > 0 && j < (width - 1))
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i][j - 1].rgbtRed +
                                 i_c[i][j + 1].rgbtRed + i_c[i + 1][j].rgbtRed +
                                 i_c[i + 1][j - 1].rgbtRed + i_c[i + 1][j + 1].rgbtRed) /
                                6.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i][j - 1].rgbtGreen +
                                   i_c[i][j + 1].rgbtGreen + i_c[i + 1][j].rgbtGreen +
                                   i_c[i + 1][j - 1].rgbtGreen + i_c[i + 1][j + 1].rgbtGreen) /
                                  6.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i][j - 1].rgbtBlue +
                                  i_c[i][j + 1].rgbtBlue + i_c[i + 1][j].rgbtBlue +
                                  i_c[i + 1][j - 1].rgbtBlue + i_c[i + 1][j + 1].rgbtBlue) /
                                 6.0);
            }
            // change lower edge
            if (i == (height - 1) && j > 0 && j < (width - 1))
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i - 1][j].rgbtRed +
                                 i_c[i - 1][j - 1].rgbtRed + i_c[i - 1][j + 1].rgbtRed +
                                 i_c[i][j + 1].rgbtRed + i_c[i][j - 1].rgbtRed) /
                                6.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i - 1][j].rgbtGreen +
                                   i_c[i - 1][j - 1].rgbtGreen + i_c[i - 1][j + 1].rgbtGreen +
                                   i_c[i][j + 1].rgbtGreen + i_c[i][j - 1].rgbtGreen) /
                                  6.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i - 1][j].rgbtBlue +
                                  i_c[i - 1][j - 1].rgbtBlue + i_c[i - 1][j + 1].rgbtBlue +
                                  i_c[i][j + 1].rgbtBlue + i_c[i][j - 1].rgbtBlue) /
                                 6.0);
            }
            // upper right corner
            if (i == 0 && j == (width - 1))
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i][j - 1].rgbtRed +
                                 i_c[i + 1][j - 1].rgbtRed + i_c[i + 1][j].rgbtRed) /
                                4.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i][j - 1].rgbtGreen +
                                   i_c[i + 1][j - 1].rgbtGreen + i_c[i + 1][j].rgbtGreen) /
                                  4.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i][j - 1].rgbtBlue +
                                  i_c[i + 1][j - 1].rgbtBlue + i_c[i + 1][j].rgbtBlue) /
                                 4.0);
            }
            // upper left corner
            if (i == 0 && j == 0)
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i][j + 1].rgbtRed +
                                 i_c[i + 1][j + 1].rgbtRed + i_c[i + 1][j].rgbtRed) /
                                4.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i][j + 1].rgbtGreen +
                                   i_c[i + 1][j + 1].rgbtGreen + i_c[i + 1][j].rgbtGreen) /
                                  4.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i][j + 1].rgbtBlue +
                                  i_c[i + 1][j + 1].rgbtBlue + i_c[i + 1][j].rgbtBlue) /
                                 4.0);
            }
            // lower left corner
            if (i == (height - 1) && j == 0)
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i][j + 1].rgbtRed +
                                 i_c[i - 1][j + 1].rgbtRed + i_c[i - 1][j].rgbtRed) /
                                4.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i][j + 1].rgbtGreen +
                                   i_c[i - 1][j + 1].rgbtGreen + i_c[i - 1][j].rgbtGreen) /
                                  4.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i][j + 1].rgbtBlue +
                                  i_c[i - 1][j + 1].rgbtBlue + i_c[i - 1][j].rgbtBlue) /
                                 4.0);
            }
            // lower right corner
            if (i == (height - 1) && j == (width - 1))
            {
                new_red = round(((float) i_c[i][j].rgbtRed + i_c[i][j - 1].rgbtRed +
                                 i_c[i - 1][j - 1].rgbtRed + i_c[i - 1][j].rgbtRed) /
                                4.0);
                new_green = round(((float) i_c[i][j].rgbtGreen + i_c[i][j - 1].rgbtGreen +
                                   i_c[i - 1][j - 1].rgbtGreen + i_c[i - 1][j].rgbtGreen) /
                                  4.0);
                new_blue = round(((float) i_c[i][j].rgbtBlue + i_c[i][j - 1].rgbtBlue +
                                  i_c[i - 1][j - 1].rgbtBlue + i_c[i - 1][j].rgbtBlue) /
                                 4.0);
            }
            image[i][j].rgbtRed = new_red;
            image[i][j].rgbtGreen = new_green;
            image[i][j].rgbtBlue = new_blue;
        }
    }

    return;
}
