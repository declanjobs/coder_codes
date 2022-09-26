from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        from collections import Counter
        from heapq import heappop, heappush

        words = Counter(words)

        heap = []

        for w in words:

            heappush(heap, [-words[w], w])


        ans = []

        while len(ans) < k and heap:

            ans.append(heappop(heap)[1])


        return ans
