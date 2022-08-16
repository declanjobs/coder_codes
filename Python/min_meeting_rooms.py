class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        if len(intervals) == 0:
            return 0

        # sorted
        start_time = [intervals[i].start for i in range(len(intervals))]
        end_time = [intervals[i].end for i in range(len(intervals))]
        #all_time = start_time + end_time

        start_time.sort()
        end_time.sort()
        #all_time.sort()

        #print(start_time)
        #print(end_time)

        active = 0
        ans = 0

        j = 0
        for i in range(len(intervals)):

            active += 1

            if start_time[i] >= end_time[j]:
                active -= 1
                j += 1

            ans = max(ans, active)

        return ans


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        if len(intervals) == 0:
            return 0

        # sorted
        start_time = [intervals[i].start for i in range(len(intervals))]
        end_time = [intervals[i].end for i in range(len(intervals))]
        all_time = start_time + end_time

        start_time.sort()
        end_time.sort()
        all_time.sort()

        active = 0
        ans = 0

        for i in all_time:

            if i in start_time:
                active += 1

            if i in end_time:
                active -= 1

            ans = max(ans, active)

        return ans
