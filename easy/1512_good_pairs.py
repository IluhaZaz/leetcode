class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        l = len(nums)
        c: int = 0
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] == nums[j]:
                    c += 1
        return c