class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x**2 for x in nums])