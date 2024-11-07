class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        y = len(s) 
        j = 0
        count = 0
        if y == 0: # covering an edge case, where the length of string can be zero and output should be true
            return True

        for i in t:
            if s[j] == i:   # I am writing s[j] first, because s[j] can be one single string element
                j+=1
                count += 1
            else:
                continue
            if y == count: # the ultimate goal is to reach the count equivalent to length of string if it's reached, our job is done because count and length of string is equal.
                return True
                
        return False
        
