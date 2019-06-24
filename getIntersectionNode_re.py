'''
Quest:
    Write a program to find the node at which the intersection of two singly linked lists begins.

Solution:
    - the key is, given two linkedlist A and B, it takes the same time to traverse from B -> A and from A -> B
        if no intersection: it will meet at the end (None)
        if has intersection: A = a + c, B = b + c, a >= b, then we can see that a + c + b = b + c + a
            so it will meet at the beginning point
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa
