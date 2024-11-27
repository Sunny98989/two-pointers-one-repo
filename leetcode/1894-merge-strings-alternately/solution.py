class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        l = min(len(word1),len(word2))
        for i in range(l):
            output.append(word1[i])  
            output.append(word2[i])
        if len(word1)>l:
            output.append(word1[l:])
        if len(word2)>l:
            output.append(word2[l:])
            
        return "".join(output)
