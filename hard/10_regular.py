class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l = len(s)
        for i in range(l):
            if i >= len(p):
                return False
            if s[i] != p[i] and p[i] not in (".", "*"):
                return False
            if p[i] == '.':
                p = p.replace(p[i], s[i], 1)
            elif p[i] == '*':
                j: int = i
                while s[j] == s[i] and j < l - 1:
                    j +=1
                p = p.replace("*", s[i:j + 1], 1)
        return p == s
    

s = Solution()
print(s.isMatch("aa", "a*"))