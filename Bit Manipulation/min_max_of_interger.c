#include "bit_manipulation.h"

int findMin(int x, int y) {
    return y ^ ((x ^ y) & -(x < y));
}

int findMax(int x, int y) {
    return x ^ ((x ^ y) & -(x < y));
}
