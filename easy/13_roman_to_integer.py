class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        indx = 0
        while indx < len(s) - 1:
            temp = nums[s[indx]] - nums[s[indx + 1]]
            if temp >= 0:
                i += nums[s[indx]]
                indx += 1
            else:
                i -= temp
                indx += 2
        if indx == len(s) - 1:
            i += nums[s[indx]]
        return i
    
s = Solution()
print(s.romanToInt("MCMXCIV"))
        