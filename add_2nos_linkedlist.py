# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        base = l = ListNode(0)
        res = 0
        carry = 0
        while l1 or l2 or carry:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            res = carry+a+b
            
            
            carry = res/10
            res = res%10
            
            l.next = ListNode(res)
            l = l.next
            
        return base.next 