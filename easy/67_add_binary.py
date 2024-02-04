class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        len_a = len(a)
        len_b = len(b)
        a = "0" + a
        b = "0" + b
        if(len_a > len_b):
            b = "0"*(len_a-len_b) + b
        elif (len_b > len_a):
            a = "0"*(len_b - len_a) + a
        carry = 0
        i = -1
        while i >= -max(len_a, len_b) or carry:
            a_i = int(a[i])
            b_i = int(b[i])
            sum = a_i + b_i + carry
            if sum >= 2:
                res += str((sum)%2)
                carry = 1
            else:
                res += str(sum)
                carry = 0
            i-=1
        return res[::-1]


s = Solution()
print(s.addBinary("100", "110010"))

