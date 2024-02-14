class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while ans >= 10:
            num = ans
            ans = 0
            while num != 0:
                ans += num%10
                num//=10
        return ans
            






    """def addDigits(self, num: int) -> int:
        num = str(num)
        if len(num) == 1:
            return int(num)
        return self.addDigits(sum([int(i) for i in num]))
"""