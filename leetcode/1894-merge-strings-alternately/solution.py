class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        maxlen = max(len1,len2)
        merged = []
        i = 0
        for i in range(maxlen):
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])

        return "".join(merged)
