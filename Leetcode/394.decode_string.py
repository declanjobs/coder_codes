class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:

            if c == "]":
                temp = ""

                while stack and stack[-1] != "[":
                    # Need to reverse the popped string
                    # bc the string will be reversed again
                    temp += stack.pop()[::-1]

                # reverse
                temp = temp[::-1]

                # pop "["
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k += stack.pop()

                k = k[::-1]
                k = int(k)

                #print(temp, k)
                temp = temp * k

                stack.append(temp)

            else:
                stack.append(c)


        return "".join(stack)