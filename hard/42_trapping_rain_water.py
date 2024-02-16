#class Solution:

#    @staticmethod
#    def find_left(nums: list[int], start: int):
#        l = len(nums)
#        for i in range(start, l):
#            if nums[i] != 0:
#                return i
#        return -1

#    @staticmethod
#    def find_right(nums: list[int], start: int):
#        l = len(nums)
#        h: int = 0
#        for i in range(start + 1, l):
#            if nums[i] > nums[start]:
#                h = nums[i]
#                break
#        if h != 0:
#            for i in range(start + 1, l):
#                if nums[i] == h:
#                    return i

#        ind: int = 0
#        for i in range(start + 1, l):
#            if nums[i] >= h:
#                h = nums[i]
#                ind = i
#        if ind:
#            return ind
#        return -1
            
#    def trap(self, height: list[int]) -> int:
#        left:int = 0
#        water: int = 0
#        l = len(height)
#        left = self.find_left(height, 0)
#        right = self.find_right(height, left)
#        while right != -1 and left != -1:
#            h = min(height[left], height[right])
#            for i in range(left + 1, right):
#                water += h - height[i]
#            left = right
#            right = self.find_right(height, left)
#        return water
        

s = Solution()
print(s.trap([4,2,0,3,2,5]))     