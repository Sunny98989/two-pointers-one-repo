class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        word = list(s)
        vowels = ["a", "A", "e", "E", "I", "i", 'O', 'o', "u", "U"]
        while start<end:
            while start < end and word[start] not in vowels:
                start += 1
            while start < end and word[end] not in vowels:
                end -= 1
            word[start], word[end] = word[end], word[start]
            start+=1
            end-=1
        return "".join(word)
