from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        # write your code here

        total = len(a) + len(b)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        a_l, a_r = 0, len(a) - 1

        while True:

            a_mid = (a_l + a_r) // 2
            b_mid = half - a_mid - 2

            aleft = a[a_mid] if a_mid >= 0 else float("-inf")
            aright = a[a_mid+1] if a_mid+1 < len(a) else float("inf")
            bleft = b[b_mid] if b_mid >= 0 else float("-inf")
            bright = b[b_mid+1] if b_mid+1 < len(b) else float("inf")


            if aleft <= bright and aright >= bleft:

                if total % 2:
                    return min(aright, bright)
                else:
                    return (min(aright, bright) + max(aleft, bleft)) / 2

            elif aleft > bright:
                a_r = a_mid - 1
            else:
                a_l = a_mid + 1