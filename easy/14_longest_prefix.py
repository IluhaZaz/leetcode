class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref: str = ""
        for let in zip(*tuple(x for x in strs)):
            let = sorted(let)
            if let[0] == let[-1]:
                pref += let[0]
            else:
                break
        return pref


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
