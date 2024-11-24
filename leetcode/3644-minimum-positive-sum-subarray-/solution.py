class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')  # Initialize to infinity to find the minimum

    # Loop through all subarray lengths from L to R
        for size in range(l, r + 1):
            current_sum = sum(nums[:size])  # Initial sum for the first subarray of this size
    
            # Check if the first subarray has a positive sum
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)
    
            # Slide the window and calculate the sum for remaining subarrays of this size
            for i in range(size, len(nums)):
                current_sum += nums[i] - nums[i - size]  # Slide the window
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)  # Update min_sum if we find a smaller positive sum
    
        # Return the minimum sum found, or -1 if no valid subarray was found
        return min_sum if min_sum != float('inf') else -1

                
