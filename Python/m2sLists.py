# Problem 21: Merge Two Sorted Lists
from typing import Optional

#Definition for a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Tasked to merge two lists into one sorted lists
        # first initialize a dummy head, then set a node to point to that head
        dummy_node = ListNode()
        curr = dummy_node # curr is a pointer that points to the dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                #that means we'd want to connect to list1
                curr.next = list1 # point/connect to list1
                curr = list1 # set the current pointer to list1
                list1 = list1.next # moving list1 over

            else:
                curr.next = list2 # point/connect to list2
                curr = list2 # set the current pointer to list2
                list2 = list2.next # moving list2 over

        curr.next = list1 if list1 else list2

        return dummy_node.next # our original node was set at the dummy node