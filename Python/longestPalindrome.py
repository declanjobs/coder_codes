
class Solution(object):

    def __init__(self, s):

        print(self.longestPalindrome(s))

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0]*len(s) for _ in range(len(s))]

        max_i = 0
        max_j = 0
        max_len = 0

        for i in range(len(s), -1, -1):

            for j in range(i, len(s)):
                print(i,j)
                print( s[i], s[j])

                if (i == j):
                    dp[i][j] = 1

                elif s[i] == s[j]:


                    if i + 1 == j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]




                if dp[i][j] and (j-i)>max_len:
                    print("new max")
                    print( s[i], s[j])

                    max_i = i
                    max_j = j
                    max_len = j-i

        print(dp)
        return s[max_i:max_j+1]

if __name__ == '__main__':
    s = "bb"
    Solution(s)