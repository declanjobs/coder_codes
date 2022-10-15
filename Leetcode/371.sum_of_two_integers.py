class Solution:
    def getSum(self, a: int, b: int) -> int:

        carry = 0
        loc = 0
        ans = 0

        while (a or b or carry) and (loc < 32):

            ans |= (a & (1 << loc)) ^ (b & (1 << loc)) ^ (carry << loc)

            carry = (((a & (1 << loc)) & (b & (1 << loc))) | (((a & (1 << loc)) | (b & (1 << loc))) & (carry << loc)))  >> loc

            a &= ~(1 << loc)
            b &= ~(1 << loc)

            #print(ans, carry)

            loc += 1

        if ans >> 31:
            ans = ~ans
            ans = self.getSum(ans, 1)
            ans = -ans

        return ans