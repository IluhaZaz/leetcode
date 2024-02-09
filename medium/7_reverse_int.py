class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        if x >= 0:
            s = int(s)
        else:
            s = int("-" + s[:-1])
        if -2**31 <= s <= 2**31:
            return s
        return 0