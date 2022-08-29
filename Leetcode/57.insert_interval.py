from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []
        inserted = False
        for i in range(len(intervals)):
            #print(newInterval)
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])

            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans += intervals[i:]
                inserted = True
                break
            else:

                if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:

                    newInterval[0] = intervals[i][0]

                if newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:

                    newInterval[1] = intervals[i][1]


        if not inserted:
            ans.append(newInterval)

        #print(ans)

        return ans


