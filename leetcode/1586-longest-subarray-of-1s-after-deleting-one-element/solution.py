class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        num_0s = 1

        for r in range(len(nums)):
            if nums[r] == 0:
                num_0s -= 1
            if num_0s<0:
                if nums[l] == 0:
                    num_0s += 1
                l += 1
        return r - l
            
        
