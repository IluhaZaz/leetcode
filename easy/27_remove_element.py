class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort(key=lambda x: 1 if x == val else 0)
        return len(nums) - nums.count(val)

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2], 2))