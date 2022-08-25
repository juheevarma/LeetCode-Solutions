# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, last = head, head
        size = self.getLength(head)
        while last:
            temp = []
            if size >= k:
                for i in range(k):
                    temp.append(last.val)
                    last = last.next
                for i in range(k):
                    first.val = temp.pop()
                    first = first.next
            else:
                break
            size -= k
        return head
    
    def getLength(self, head) -> int:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length
