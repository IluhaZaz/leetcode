class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points = [x[0] for x in points]
        points.sort()
        l = 0
        for i in range(len(points) - 1):
            l = max(points[i + 1] - points[i], l)
        return l

s = Solution()
s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])