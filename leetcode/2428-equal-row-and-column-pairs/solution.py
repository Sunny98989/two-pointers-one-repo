class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        count = 0
        for row in grid:
            d[str(row)] = d.get(str(row),0) + 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += d[str(col)]
        return count
