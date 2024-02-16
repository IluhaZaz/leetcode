class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        p: int = sum(nums)
        for i in nums:
            p -= i
            if p > i:
                return p + i
        return -1
    
s = Solution()
print(s.largestPerimeter([1,12,1,2,5,50,3]))