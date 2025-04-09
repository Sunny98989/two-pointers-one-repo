class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_Sum = max_Sum = nums[0]
        for i in nums[1:]:
            curr_Sum = max(curr_Sum+i, i)
            max_Sum = max(curr_Sum, max_Sum)
        return max_Sum
