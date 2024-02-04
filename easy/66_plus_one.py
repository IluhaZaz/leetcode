class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        i = -1
        while carry:
            carry = 0
            if i < -len(digits):
                digits.insert(0, 0)
            if digits[i] == 8 and carry:
                digits[i] = 0
                carry = 1
            elif  digits[i] == 8 and carry:
                digits[i] = 1
                carry = 1
            elif  digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] +=1
            i-=1

        return digits
    
s = Solution()
print(s.plusOne([9,9]))