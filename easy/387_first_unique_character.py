class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_copy = s
        for let in s_copy:
            if s_copy.count(let) != 1:
                s_copy = s_copy.replace(let, "")
            else:
                return s.find(let)
        return -1
        

            

s = Solution()
print(s.firstUniqChar("aaabba"))