class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i in "[{(":
                lst.append(i)
        else:
            pass

        
            
s = Solution()
print(s.isValid("()"))