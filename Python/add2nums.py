# problem number 2

from typing import Optional

class ListNode:
    # first define a linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize a dummy head, set the current value to be the head, and the carry value to be 0
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
            # checks if both lists 1 and 2 aren't none 
            # x is the value of l1
            # y is the value of l2
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = carry + x + y
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next
    