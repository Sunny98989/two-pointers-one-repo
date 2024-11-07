class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Position where the next non-zero element should be placed
        last_non_zero = 0

        # Go through each number in the list
        for i in range(len(nums)):

            if nums[i] != 0:  # If the current number is not zero
                # Swap the current number with the position at last_non_zero
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                
                last_non_zero += 1

