from typing import List

# Bellman-Ford Algo
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        min_price = [float("inf") for _ in range(n)]
        min_price[src] = 0

        for _ in range(k+1):
            temp_min = min_price.copy()
            for s, d, p in flights:
                if min_price[s] == float("inf"):
                    continue

                if min_price[s] + p < temp_min[d]:
                    temp_min[d] = min_price[s] + p

            min_price = temp_min


        #print(min_price)
        return -1 if min_price[dst] == float("inf") else min_price[dst]