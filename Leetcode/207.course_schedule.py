from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        from collections import defaultdict, deque

        course_tree = defaultdict(list)
        prep_count = [0] * numCourses

        for p in prerequisites:
            c, p = p[0], p[1]
            course_tree[p].append(c)
            prep_count[c] += 1


        #print(prep_count)
        course_taken = set()

        q = deque([])

        for c in range(numCourses):
            if prep_count[c] != 0:
                continue
            q.append(c)

        while q:
            c = q.popleft()
            course_taken.add(c)

            for sub in course_tree[c]:
                prep_count[sub] -= 1
                if sub not in course_taken and prep_count[sub] == 0:
                    q.append(sub)

        return True if len(course_taken) == numCourses else False