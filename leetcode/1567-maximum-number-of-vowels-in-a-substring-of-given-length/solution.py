class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        currentVowels = sum(1 for c in s[:k] if c in "aeiou")
        maxVowels = currentVowels
        
        for i in range(k, len(s)):
            if s[i] in "aeiou":
                currentVowels += 1
            if s[i-k] in "aeiou":
                currentVowels -= 1
            if currentVowels > maxVowels:
                maxVowels = currentVowels
            elif maxVowels == k:
                break
        return maxVowels

        
            
