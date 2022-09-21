#include "bit_manipulation.h"

// Function to turn off k'th bit in `n`
int turnOffKthBit(int n, int k) {
    return n & ~(1 << (k - 1));
}

// Function to turn on k'th bit in `n`
int turnOnKthBit(int n, int k) {
    return n | (1 << (k - 1));
}

// Function to check if k'th bit is set for `n` or not
uint8_t isKthBitSet(int n, int k) {
    return (n & (1 << (k - 1))) != 0;
}

// Function to toggle k'th bit of `n`
int toggleKthBit(int n, int k) {
    return n ^ (1 << (k - 1));
}