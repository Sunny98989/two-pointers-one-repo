
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        d = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in d:
                    d[grid[i][j]]=0
                d[grid[i][j]] +=1

        for i in range(1,n*n+1):
            if i not in d:
                missing = i
            elif i in d and d[i] == 2:
                double = i
        return [double,missing]
