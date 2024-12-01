class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in arr:
            d[i] = d.get(i,0)+1
        l = list(d.values())
        return len(l) == len(set(l))
