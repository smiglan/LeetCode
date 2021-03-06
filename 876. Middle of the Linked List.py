# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:57:58 2020

@author: migla
"""
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Note:

# The number of nodes in the given list will be between 1 and 100.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #Output to array
#         node = head
#         a = []
#         length = 0
#         while node:
#             a.append(node)
#             node = node.next
#             length += 1
#         print(length)

#         return a[int(length/2)]
        
        #Slow and Fast Pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # while index < i:
        #     node = node.next
        #     index += 1
        # return node
        # # if len(a)%2 == 0:
            
        