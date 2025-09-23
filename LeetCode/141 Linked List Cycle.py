class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        l = 0
        while l<10**4+1:
            if node == None:
                return False
            node = node.next
            l += 1
        return True