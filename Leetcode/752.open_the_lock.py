from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        if target == "0000":
            return 0

        if "0000" in deadends:
            return -1

        visited = set(deadends)
        q = deque([["0000", 0]])

        def next_pin(p):

            for i in range(4):
                n = int(p[i])

                n_fwd = str((n + 1) % 10)[:1]
                yield (p[:i] + (n_fwd) + p[i+1:])

                n_bck = str((n - 1 + 10) % 10)[:1]
                yield (p[:i] + (n_bck) + p[i+1:])


        while q:

            pin, step = q.popleft()

            if pin in visited:
                continue
            visited.add(pin)

            for p in next_pin(pin):

                if p == target:
                    return step + 1

                if p not in visited:
                    visited.add(pin)
                    q.append([p, step+1])


        return -1