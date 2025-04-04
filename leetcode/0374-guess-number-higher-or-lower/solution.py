# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0d
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the search range
        low = 1  # The smallest possible number
        high = n  # The largest possible number

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Find the middle number
            
            res = guess(mid)  # Call the provided API to check the guessed number

            if res == 0:
                return mid  # If guess(mid) == 0, we found the correct number
            
            if res == 1:
                # If guess(mid) == 1, it means the picked number is higher than mid.
                # So, we adjust our search range by moving 'low' up.
                low = mid + 1
            else:
                # If guess(mid) == -1, it means the picked number is lower than mid.
                # So, we adjust our search range by moving 'high' down.
                high = mid - 1
        
        # If we exit the loop, it means no valid number was found, return -1 (this shouldn't happen in a valid case)
        return -1
