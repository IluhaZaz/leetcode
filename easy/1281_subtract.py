class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s: int = 0
        prod: int = 1
        while n != 0:
            temp = n%10
            s += temp
            prod *= temp
            n//=10
        return prod - s