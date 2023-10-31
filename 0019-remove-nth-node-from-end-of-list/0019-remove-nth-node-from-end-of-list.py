# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return 
        length = 1
        temp = head
        while temp.next != None:
            length+=1
            temp = temp.next
        required_traverses = length - n
        if  required_traverses ==0:
            temp = head
            head = temp.next
            del temp
            return head
        temp = head
        for i in range(required_traverses-1):
            temp = temp.next
        if temp == head and n==2 and length==2:
            h = head
            head = h.next
            del h
            return head
        tobe = temp.next
        if tobe:
            temp.next = tobe.next
            del tobe
        return head




            
