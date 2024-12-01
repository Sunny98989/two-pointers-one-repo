class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in word1:
            d1[i] = d1.get(i, 0)+1
        for i in word2:
            d2[i] = d2.get(i, 0)+1
        l1 = list(d1.values())
        l2 = list(d2.values())
        return sorted(l1) == sorted(l2)
