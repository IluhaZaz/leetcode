class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = []
        tt = []
        for i in s:
            ss.append(s.index(i))
        for i in t:
            tt.append(t.index(i))
        return ss == tt
