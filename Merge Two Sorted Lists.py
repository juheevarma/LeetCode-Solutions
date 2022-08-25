class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        ptr = dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
            
        if l1:
            ptr.next = l1
        else:
            ptr.next = l2
            
        return dummy.next
