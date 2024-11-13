class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        if len(nums)<0:
            return 0

        if len(nums) == 1:
            return float(nums[0])


        current_sum = sum(nums[:k])
        max_sum = current_sum


        for i in range(k,len(nums)):
            
            current_sum = current_sum - nums[i-k] + nums[i]

            if current_sum > max_sum:
                max_sum = current_sum


        return max_sum/k

