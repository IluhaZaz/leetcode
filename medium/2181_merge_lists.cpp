struct ListNode {
     int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        while(head->val == 0){
            head = head->next;
        }

        ListNode* temp1 = head;
        ListNode* temp2 = head->next;
        while(temp2){
            while (temp2->val != 0)
            {
                temp1->val += temp2->val;
                temp2 = temp2->next;
            }
            
            while(temp2->val == 0){
                temp2 = temp2->next;
                if(!temp2){
                    temp1->next = nullptr;
                    return head;
                }
            }

            temp1->next = temp2;
            
            temp1 = temp2;
            temp2 = temp1->next;
        }
        return head;
    }
};