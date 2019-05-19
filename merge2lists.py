class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = 0
        ptr2 = 0
        base = l = ListNode(0)
        while l1 and l2:
             if l1.val > l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
        
        if l1:
            while l1:
                l.next = ListNode(l1.val)
        else:
            while l2:
                l.next = ListNode(l2.val)
        return base.next