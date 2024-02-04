class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        while True:
            left += 1
            if left*left > x:
                left -= 1
                break
        return left

s = Solution()
print(s.mySqrt(4))