class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not len(s):
            return ""

        max_len = 1
        ans = s[0]

        for i in range(len(s)):

            left, right = i, i
            while 0<=left<=right<len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    ans = s[left:right+1]
                    max_len = right - left + 1

                left -= 1
                right += 1

            left, right = i, i+1
            while 0<=left<=right<len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    ans = s[left:right+1]
                    max_len = right - left + 1

                left -= 1
                right += 1

        return ans

    # The DP solutions is actually mush slower
    def longestPalindrome_dp(self, s: str) -> str:
        if not len(s):
            return ""

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        max_len = 1
        ans = s[0]
        for i in range(len(s)-1, -1, -1):

            for j in range(i+1, len(s)):

                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 1
                    elif j - i > 1 and dp[i+1][j-1]:
                        dp[i][j] = 1

                if dp[i][j]:
                    #print(i, j)
                    if j - i + 1 > max_len:
                        ans = s[i:j+1]
                        max_len = j - i + 1

                        #print(max_len)

        return ans