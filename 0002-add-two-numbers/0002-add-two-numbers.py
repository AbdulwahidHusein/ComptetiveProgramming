# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #first
        curval  = 0
        carry=0
        answerNode = ListNode()
        curval = (l1.val+l2.val)%10+carry
        carry = int((l1.val+l2.val)/10)
        answerNode.val = curval
        #then
        curval  = 0
        temp1 = l1.next
        temp2 = l2.next
        baseNode = answerNode
        while temp1 and temp2:
            newn = ListNode()
            answerNode.next = newn
            answerNode = newn
            curval = (temp1.val+temp2.val+carry)%10
            carry = int((temp1.val+temp2.val+carry)/10)
            answerNode.val = curval
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            curval = (temp1.val+carry)%10
            carry = int((temp1.val+carry)/10)
            newn = ListNode()
            answerNode.next = newn
            answerNode = newn
            answerNode.val = curval
            temp1 = temp1.next
        while temp2:
            curval = (temp2.val+carry)%10
            carry = int((temp2.val+carry)/10)
            newn = ListNode()
            answerNode.next = newn
            answerNode = newn
            answerNode.val = curval
            temp2 = temp2.next
        if carry:
            newn = ListNode()
            answerNode.next = newn
            answerNode = newn
            answerNode.val = carry



        return baseNode
