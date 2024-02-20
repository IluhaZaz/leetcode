from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid: str = ascii_lowercase + digits
        buf: str = ""
        for i in s.lower():
            if i in valid:
                buf += i
        return buf == buf[::-1]