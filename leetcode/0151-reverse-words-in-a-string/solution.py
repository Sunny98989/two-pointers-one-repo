class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = s.split() 
        reversed_new_string = reversed(new_string)
        return ' '.join(reversed_new_string)
