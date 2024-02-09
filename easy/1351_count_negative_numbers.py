class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        c = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    c += n - j
                    break
        return c
    
s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
        