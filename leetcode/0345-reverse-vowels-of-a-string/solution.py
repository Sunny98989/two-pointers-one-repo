class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        f = 0
        l = len(s)-1
        word = list(s)
        while f<l:
            while f<l and word[f] not in vowels:
                f+=1
            while f<l and word[l] not in vowels:
                l-=1
            word[f], word[l] = word[l], word[f]
            l-=1
            f+=1
        
        return ''.join(word)
