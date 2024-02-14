class Solution:
    @staticmethod
    def find_negative(nums: list[int], ind: int):
        if(ind >= len(nums)):
            return -1
        while(nums[ind] >= 0 and ind < len(nums)):
            if ind + 1 >= len(nums):
                return -1
            ind += 1
        if(ind >= len(nums)):
            return -1
        return ind
    
    @staticmethod
    def find_positive(nums: list[int], ind: int):
        if(ind >= len(nums)):
            return -1
        while(nums[ind] < 0):
            if ind + 1 >= len(nums):
                return -1
            ind += 1
        if(ind >= len(nums)):
            return -1
        return ind

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        buf: list[int] = []
        p = self.find_positive(nums, 0)
        n = self.find_negative(nums, 0)
        while(p != -1 and n != -1):
            buf.append(nums[p])
            buf.append(nums[n])
            p = self.find_positive(nums, p + 1)
            n = self.find_negative(nums, n + 1)
        if p == -1 and n == -1:
            return buf
        elif p == -1:
            buf.append(nums[n])
        elif n == -1:
            buf.append(nums[p])
        return buf
    
s = Solution()
print(s.rearrangeArray([-1,1]))