# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
#8:12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #Input: head = [4,5,1,9], node = 5
        #Output: [4,1,9]
        #Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function. 
        
        node.val = node.next.val
        node.next = node.next.next
        