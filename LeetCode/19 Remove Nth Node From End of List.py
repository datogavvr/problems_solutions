class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        if l <= 1:
            return
        if l == n:
            return head.next
        node = head
        for i in range(l-n-1):
            node = node.next
        node.next = node.next.next
        return head