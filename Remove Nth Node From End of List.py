# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
#46:47

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Input: head = [1,2,3,4,5], n = 2
        # Output: [1,2,3,5]

        node = head
        element_before = None
        #Delete the only element present
        if not node.next:
            return None
        #Find element before 'to delete element'
        while node.next:
            if n > 0:
                n -= 1
                node = node.next
                if n == 0:
                    element_before = head
                    n -= 1
            else:
                node = node.next
                element_before = element_before.next
        #if no element before, delete first element
        if not element_before:
            head = head.next
        #if no element after, delete last element
        elif not element_before.next.next:
            element_before.next = None
        else:
            element_before.next = element_before.next.next
        return head
