#include "bit_manipulation.h"

/*
The idea is to use the expression (n+mask)^mask for computing the absolute value of n,
 where mask is n >> 31 (assuming 32–bit storage for integers). The mask n >> 31 will
 be evaluated to 0 for positive numbers and -1 for negative numbers. For instance,
*/

/*
it shifts all of the bits to the right and then fills in the upper bits
with a copy of whatever the last bit was

10000000 >> 31 = 11111111

*/
void abs(int32_t * n)
{
    int32_t mask = *n >> sizeof(int32_t) * 8 - 1; // mask is the sign bit
    *n = (*n + mask) ^ mask;
}