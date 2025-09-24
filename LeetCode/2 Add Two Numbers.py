class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        n1 = ''
        while node:
            n1 += str(node.val)
            node = node.next
        node = l2
        n2 = ''
        while node:
            n2 += str(node.val)
            node = node.next
        res_str = str(int(n1[::-1]) + int(n2[::-1]))[::-1]
        res = ListNode()
        node = res
        for i in res_str[:-1]:
            node.val = int(i)
            node.next = ListNode()
            node = node.next
        node.val = int(res_str[-1])
        return res