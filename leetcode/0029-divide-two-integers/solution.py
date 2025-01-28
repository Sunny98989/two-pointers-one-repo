class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Max 32-bit integer value

        # Determine the sign of the result
        sign = (dividend < 0) == (divisor < 0)  # True if same sign, else False

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize result
        ans = 0

        # Perform bitwise division
        while dividend >= divisor:
            count = 0
            while dividend >= (divisor << count):
                count += 1

            # Subtract the largest shifted divisor and add to result
            dividend -= divisor << (count - 1)
            ans += 1 << (count - 1)

        # Apply sign to the result
        return ans if sign else -ans

