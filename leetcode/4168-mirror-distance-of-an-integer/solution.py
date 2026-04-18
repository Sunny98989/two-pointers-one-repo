class Solution:
    def mirrorDistance(self, n: int) -> int:
        str_of_n = str(n)
        reversed_str = str_of_n[::-1]
        result = abs(n-int(reversed_str))
        return result
