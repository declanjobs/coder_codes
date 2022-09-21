#include "bit_manipulation.h"

// Function to swap b–bits starting from position `p` and `q` in an integer `n`
int swap(int n, int p, int q, int b)
{
    // take XOR of bits to be swapped
    int x = ((n >> p) ^ (n >> q));

    // only consider the last b–bits of `x`
    x = x & ((1 << b) - 1);

    // replace the bits to be swapped with the XORed bits
    // and take its XOR with `n`
    return n ^ ((x << p) | (x << q));
}


/*
Input:

n = 15 (15 in binary is 00001111)
p = 2, q = 5 (3rd and 6th bit from the right)
b = 2 (Total number of consecutive bits in each sequence)

Output: 99

(99 in binary is 01100011)
*/