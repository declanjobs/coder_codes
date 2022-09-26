#include "bit_manipulation.h"

// 00010100 -> 00010000
void unset_rightmost_bit(uint32_t * n)
{
    *n = *n & (*n - 1);
}

uint8_t check_if_int_power_of_two(uint32_t * n)
{
    unset_rightmost_bit(n);
    return (*n == 0);
}

// Returns the position of the rightmost set bit of `n`
int positionOfRightmostSetBit(int n)
{
    // if the number is odd, return 1
    if (n & 1) {
        return 1;
    }

    // unset rightmost bit and xor with the number itself
    n = n ^ (n & (n - 1));

    // find the position of the only set bit in the result;
    return log2(n) + 1;
}

// Function to find parity of number `n`
bool findParity(uint32_t n)
{
    bool parity = false;

    // run till `n` becomes 0
    while (n)
    {
        // invert the parity flag
        if (n & 1) {
            parity = !parity;
        }

        // right shift `n` by 1 (divide by 2)
        n = n >> 1;
    }

    return parity;
}