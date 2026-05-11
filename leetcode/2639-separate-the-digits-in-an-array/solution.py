class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:

            temp = []

            while num > 0:
                temp.append(num % 10)
                num //= 10

            while temp:
                ans.append(temp.pop())

        return ans
