class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        buf = []
        l = len(nums)
        for i in range(min(nums)):
            buf.append(i)
        for i in range(l - 1):
            buf += list(range(nums[i] + 1, nums[i + 1]))
        for i in range(max(nums) + 1, l + 1):
            buf.append(i)
        return buf
    
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))