#include "bit_manipulation.h"

// Swap using references in C++
void swap(int &x, int &y)
{
    // return if both variables' data is the same, as we can't check for the
    // address of a reference
    if (x == y) {
        return;
    }

    x = x + y;          // Note: overflow might happen
    y = x - y;
    x = x - y;
}

// Swap using pointers to a function
void swap(int *x, int *y)
{
    if (*x == *y) {     // Check if the two addresses are the same
        return;
    }

    *x = *x + *y;       // overflow might happen
    *y = *x - *y;
    *x = *x - *y;
}

void swap(int &x, int &y)
{
    if (y && x != y)
    {
        x = x * y;      // overflow can happen
        y = x / y;
        x = x / y;
    }
}

void swap(int &x, int &y)
{
    if (x != y)
    {
        x = x ^ y;
        y = x ^ y;
        x = x ^ y;
    }

    // in a single line
    // (x == y) || ((x ^= y), (y ^= x), (x ^= y));
}

void swap(int &x, int &y)
{
    if (x != y)
    {
        x = x - y;
        y = y + x;
        x = y - x;
    }

    // in a single line
    // (x == y) || ((x -= y), (y += x), (x = y - x));
}

void swap(int &x, int &y)
{
    // x = x ^ y ^ (y = x);
    // x = x + y - (y = x);
    x = (x * y) / (y = x);
}
