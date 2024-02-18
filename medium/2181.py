class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        while head.val == 0:
            head = head.next
        
        temp1: ListNode = head
        temp2: ListNode = head.next

        while temp2:
            while temp2.val != 0:
                temp1.val += temp2.val
                temp2 = temp2.next
            while temp2.val == 0:
                temp2 = temp2.next
                if not temp2:
                    temp1.next = None
                    return head
            temp1.next = temp2
            temp1 = temp2
            temp2 = temp1.next
        return head