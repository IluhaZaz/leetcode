class Solution:
    def frequencySort(self, s: str) -> str:
        alf = dict.fromkeys(set(s), 0)
        for key in alf.keys():
            alf[key] = s.count(key)
        alf = list(alf.items())
        alf = sorted(alf, key=lambda x: x[1], reverse=True)
        s = ""
        for let, num in alf:
            s+= let*num
        return s



s = Solution()
print(s.frequencySort("assaaar"))