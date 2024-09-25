class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = new ListNode();  
        ListNode* MergeList = head;  
        
        if (list1 == NULL) {
            return list2;
        }
        
        if (list2 == NULL) {
            return list1;
        }

        while (list1 != NULL && list2 != NULL) {
            if (list1->val <= list2->val) {
                MergeList->next = list1;  
                list1 = list1->next;  
            } else {
                MergeList->next = list2;  
                list2 = list2->next;  
            }
            MergeList = MergeList->next;  
        }

        
        if (list1 != NULL) {
            MergeList->next = list1;
        } else {
            MergeList->next = list2;
        }

        return head->next;  
    }
};
