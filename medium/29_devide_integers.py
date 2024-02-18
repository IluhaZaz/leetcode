class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans: int = 0
        while dividend >= divisor:
            ans += 1
            dividend -= divisor
        return ans

s = Solution()
print(s.divide(10, 3))