class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meeting_room_i_i_i(self, intervals: List[List[int]], rooms: int, ask: List[List[int]]) -> List[bool]:
        # Write your code here.

        sums = [0 for _ in range(50001)]
        ans = [False for _ in range(len(ask))]
        max_num = 0

        for i in intervals:
            sums[i[0]] += 1
            sums[i[1]] -= 1
            max_num = max(max_num , i[1])

        for i in ask:
            max_num = max(max_num , i[1])

        temp = 0
        for s in range(1, max_num + 1):
            temp += sums[s]
            if temp < rooms:
                sums[s] = 0
            else:
                sums[s] = 1

        for s in range(1, max_num + 1):
            sums[s] +=  sums[s-1]

        for i,a in enumerate(ask):
            if (sums[a[1]-1] == sums[a[0]-1]):
                ans[i] = True

        return ans