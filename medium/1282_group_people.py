class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        d = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] in d.keys():
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = []
                d[groupSizes[i]].append(i)
        ans = []
        for key, val in d.items():
            n = len(val)//key
            ans += [val[i::n] for i in range(n)]
        return ans

s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))

