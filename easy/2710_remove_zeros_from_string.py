class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != "0":
            return num
        i = -2
        while num[i] == '0':
            i-=1
        return num[:i + 1]
    
s = Solution()
print(s.removeTrailingZeros("5123010000"))