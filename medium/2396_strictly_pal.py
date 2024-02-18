class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            s = ""
            temp = n
            while n:
                s += str(n%base)
                temp/=base
            if s != s[::-1]:
                return False
        return True