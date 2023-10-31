class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)  
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            nex = curr.next
            temp = nex.next

            # Swap adjacent nodes
            prev.next = nex
            nex.next = curr
            curr.next = temp

            # Move to the next pair
            prev = curr
            curr = temp

        return dummy.next