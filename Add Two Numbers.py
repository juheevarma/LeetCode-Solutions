class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = self.getStrings(l1)
        s2 = self.getStrings(l2)
        string = str( int(s1[::-1]) + int(s2[::-1]) )[::-1]
        head = ListNode(string[0])
        temp = head
        for i in range(1, len(string)):
            nxt = ListNode(int(string[i]))
            temp.next = nxt
            temp = temp.next
        return head
    
    def getStrings(self, lst) -> str:
        res = ""
        current = lst
        while current:
            res += str(current.val)
            current = current.next
        return res
