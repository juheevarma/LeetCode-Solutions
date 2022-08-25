class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]
