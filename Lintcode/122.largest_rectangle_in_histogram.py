from typing import (
    List,
)

class Solution:
    """
    @param heights: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largest_rectangle_area(self, heights: List[int]) -> int:
        # write your code here

        max_area = 0
        stack = []
        # idx, height

        for i, h in enumerate(heights):

            _i_ = i

            while stack and stack[-1][1] > h:
                #print(stack[-1][1], h)
                ii, hh = stack.pop()

                area = (i - ii) * hh
                #print(i, ii, hh, area)

                max_area = max(max_area, area)

                _i_ = ii

            max_area = max(max_area, h)
            stack.append([min(i, _i_), h])

        #print(stack)

        right = len(heights)
        while stack:
            ii, hh = stack.pop()

            area = (right - ii) * hh
            #print(area)

            max_area = max(max_area, area)


        return max_area