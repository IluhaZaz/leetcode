class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums, key = lambda x: nums.count(x), reverse= True)
        matrix = []
        raw = 0
        l = len(nums)
        while nums:
            matrix.append([])
            i = 0
            while i < l:
                if nums[i] not in matrix[raw]:
                    matrix[raw].append(nums[i])
                    nums.remove(nums[i])
                    l -= 1
                    i -=1
                i += 1
            raw += 1
        return matrix
    
s = Solution()
print(s.findMatrix([1,3,4,1,2,3,1]))
        