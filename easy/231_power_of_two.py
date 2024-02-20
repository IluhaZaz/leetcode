from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ans = log2(n)
        return int(ans) == ans