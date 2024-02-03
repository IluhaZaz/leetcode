class Solution:

    def num_start(self, s: str, left: int):
        ind = left - 1
        if ind <= 0:
            return 0
        while s[ind - 1].isdigit() and ind != 0:
            ind -= 1
        return ind

    def decodeString(self, s: str) -> str:
        left = s.rfind("[")
        right = s.find("]", left)
        num_s = self.num_start(s, left)
        while left != -1:
            s = s.replace(s[num_s:right + 1], int(s[num_s:left])*s[left+1:right], 1)
            left = s.rfind("[")
            right = s.find("]", left)
            num_s = self.num_start(s, left)
        return s

s = Solution()
print(s.decodeString("2[a]"))