class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = head
        temp2 = head.next
        flag = 0
        while(temp2):
            if flag:
                temp.next = temp2.next
                temp = temp2
                temp2 = temp2.next
                flag = 0
            elif(temp.val == temp2.val):
                flag = 1
            else:
                temp = temp.next
                temp2 = temp2.next
        return head
    
        