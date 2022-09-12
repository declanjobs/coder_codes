from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import Counter, deque
        from heapq import heapify, heappop, heappush

        taskCount = Counter(tasks)
        maxheap = [-count for count in taskCount.values()]
        heapify(maxheap)

        #print(maxheap)

        q = deque()
        time = 0

        while q or maxheap:

            time += 1

            if maxheap:
                # plus 1 to reduce the number of remaining task
                count = heappop(maxheap) + 1

                # Not to add to q if all tasks processed
                if count:
                    q.append([count, time + n])

            # Add a task back to maxheap when it passes the cool-down
            # time for the task
            if q and q[0][1] == time:
                heappush(maxheap, q.popleft()[0])

        return time