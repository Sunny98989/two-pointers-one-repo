class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        l = 0
        r = len(s)-1
        word = list(s)
        
        while r>l:
            while word[l] not in vowels and l < r:
                l += 1
            while word[r] not in vowels and r > l:
                r -= 1
            word[l], word[r] = word[r], word[l]
            l+=1
            r-=1

        return "".join(word)
