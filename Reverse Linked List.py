# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
#15:41

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Input: head = [1,2,3,4,5]
        # Output: [5,4,3,2,1]
        if head == None:
            return None
        node = head
        prev = None
        while node.next:
            nxt = node.next
            if prev == None:
                node.next = None
            else:
                node.next = prev
            prev = node
            node = nxt
        node.next = prev
        return node