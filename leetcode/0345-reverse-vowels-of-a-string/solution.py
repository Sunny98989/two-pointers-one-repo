class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("AEIOUaeiou")
        l = 0
        r = len(s)-1
        word = list(s)
        while l<r :
            while word[l] not in vowels and l<r:
                l+=1
            while word[r] not in vowels and l<r:
                r-=1
            word[l],word[r]=word[r],word[l]
            l+=1
            r-=1
        return ''.join(word)

