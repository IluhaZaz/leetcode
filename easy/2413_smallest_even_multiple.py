class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        val = n if n%2 == 0 else n + 1
        for i in range(val, 301, 2):
            if i%n == 0:
                return i