class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        w1 = {}
        w2 = {}
        n1 = len(s)//k
        n2 = len(t)//k
        
        for i in range(0,len(s),n1):
            w1[s[i:i+n1]] = w1.get(s[i:i+n1],0)+1
        for i in range(0,len(t),n2):
            w2[t[i:i+n2]] = w2.get(t[i:i+n2],0)+1

        return w1 == w2
