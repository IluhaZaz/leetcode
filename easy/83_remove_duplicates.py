class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        temp = head
        temp2 = head
        flag = 0

        while(temp2.next):
            if temp2.next.val == temp.val:
                temp2 = temp2.next
                flag = 1
            elif flag == 0:
                temp = temp.next
                temp2 = temp2.next
            else:
                temp.next = temp2.next
                flag = 0
        if flag == 1:
                    temp.next = temp2.next
        return head