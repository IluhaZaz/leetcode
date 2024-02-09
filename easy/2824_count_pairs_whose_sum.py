import itertools

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        c = 0
        for i, j in itertools.combinations(nums, 2):
            if i + j < target:
                c+=1
        return c