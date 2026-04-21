from typing import List
from collections import Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = list(range(len(source)))
        
        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Step 1: Build connected components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Step 2: Group indices by component
        groups = {}
        for i in range(len(source)):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        # Step 3: Count mismatches
        hamming = 0
        
        for indices in groups.values():
            count = Counter()
            
            # Count frequency of source values in this component
            for i in indices:
                count[source[i]] += 1
            
            # Try matching target values
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    hamming += 1
        
        return hamming
