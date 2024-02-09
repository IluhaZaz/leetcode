class ListNode:
      def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = ""
        while head:
            s += head.val
            head = head.next
        return s == s[::-1]