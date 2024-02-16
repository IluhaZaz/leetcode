class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l = []
        l += list(filter(lambda x: 1 if x%2 == 0 else 0, nums))
        l += list(filter(lambda x: 0 if x%2 == 0 else 1, nums))
        return l