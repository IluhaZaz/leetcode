from itertools import combinations

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        for i in combinations(nums, 3):
            if sum(i) == 0:
                ans.append(list(i))
        return ans