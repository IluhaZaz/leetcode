class Solution:   
    def help(self, nums: list[int], start: int, end: int, target: int):
        if (start > end):
            return -1 
        mid: int = (start + end) // 2
        if (nums[mid] == target):
            return mid
        if (target > nums[mid]):
            return self.help(nums, mid + 1, end, target)
        return self.help(nums, start, mid - 1, target)

    def search(self, nums: list[int], target: int) -> int:
        return self.help(nums, 0, len(nums) - 1, target)
    
