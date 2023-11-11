# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena = 0
        lenb = 0
        temp1, temp2 = headA, headB

        while temp1:
            lena += 1
            temp1 = temp1.next
        while temp2:
            lenb += 1
            temp2 = temp2.next
        temp1, temp2 = headA, headB
        if lena > lenb:
            for i in range(lena-lenb):
                temp1 = temp1.next
        else:
            for i in range(lenb-lena):
                temp2 = temp2.next
        while temp1 and temp2:
            if temp1 is temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None


        