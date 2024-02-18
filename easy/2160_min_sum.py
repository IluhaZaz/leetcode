class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        while num != 0:
            l.append(num%10)
            num//=10
        l.sort()
        a = int(str(l[0]) + str(l[2]))
        b = int(str(l[1]) + str(l[3]))
        return a + b