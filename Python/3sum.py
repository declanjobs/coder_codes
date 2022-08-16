class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here

        numbers.sort()
        print(numbers)

        ans = []

        for idx, val in enumerate(numbers):
            if val > 0:
                break

            if idx > 0:
                if val == numbers[idx-1]:
                    continue

            target = -val

            for i in range(idx+1, len(numbers)):

                if i>(idx+1) and (numbers[i] == numbers[i-1]):
                    continue

                temp = target - numbers[i]
                #print(temp)
                #print(numbers[i:])

                if (temp in numbers[i+1:]):
                    #print("new")
                    #print([val, numbers[i], temp])
                    ans.append([val, numbers[i], temp])

        return ans


