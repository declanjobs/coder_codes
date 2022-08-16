class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here

        dp = [0] * (m + 1)

        dp[0] = True

        for i in range(len(a)):

            for j in range(m, -1, -1):

                if j >= a[i]:

                    dp[j] = dp[j] or dp[j - a[i]]

            #print(dp)

        for i in range(m, -1, -1):
            if dp[i]:
                return i

        return 0