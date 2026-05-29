class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = float('inf')
        for i in nums:
            sum = 0
            for j in str(i):
                sum += int(j)
            minimum = min(sum, minimum)
        return minimum
