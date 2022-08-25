class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        previous, current, i = head, head, 0
        while i != n and current:
            current = current.next
            i += 1
        if current == None: 
            return head.next 
        while current.next:
            previous = previous.next
            current = current.next
        previous.next = previous.next.next
        return head
        
    def getLength(self, head) -> int:
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1
        return length
