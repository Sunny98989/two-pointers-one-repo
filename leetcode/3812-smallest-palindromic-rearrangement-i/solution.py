class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s)
        odd_char = []
        if l == 1:
            return s

        if l%2 != 0:
            odd_char.append(s[l//2])
        
        base = sorted(s[:l//2])
    

        return "".join(base+odd_char+base[::-1])
        
