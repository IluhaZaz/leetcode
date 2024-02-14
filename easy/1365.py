class Solution:

    @staticmethod
    def count(nums: list[int], val:int):
        c: int = 0
        for i in nums:
            if val > i:
                c += 1
        return c

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        return list(map(lambda x: self.count(nums, x), nums))
        
        