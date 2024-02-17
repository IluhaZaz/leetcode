class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        buf = [0] * (n+1)
        buf[0] = 1
        buf[1] = 1
        
        for i in range(2, n+1):
            buf[i] = buf[i-1] + buf[i-2]
        return buf[n]