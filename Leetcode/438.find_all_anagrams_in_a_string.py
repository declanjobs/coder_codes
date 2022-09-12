from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        target = Counter(p)

        left, right = 0, 0

        temp = defaultdict(int)
        ans = []
        while right < len(s):

            temp[s[right]] += 1

            while right - left >= len(p):
                temp[s[left]] -= 1
                if temp[s[left]] == 0:
                    del temp[s[left]]

                left += 1

            #print(temp, target, left, right)
            if temp == target:
                ans.append(left)

            right += 1

        return ans