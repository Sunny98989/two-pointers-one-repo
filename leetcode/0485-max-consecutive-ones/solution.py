class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxC = 0

        for num in nums:
            if num == 1:
                count += 1
                if maxC >= count:
                    maxC = maxC
                else:
                    maxC = count
            else:
                count = 0

        return maxC

