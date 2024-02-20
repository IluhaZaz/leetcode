class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        curr: int = 1

        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            if nums[i] == nums[i - 1] and i != 0:
                continue
            if nums[i] > 0 and nums[i] != curr:
                return curr
            curr += 1
        return curr