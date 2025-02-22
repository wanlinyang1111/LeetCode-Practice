class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None            # Initialize previous node as None
        curr = head            # Start with the head node

        while curr:            # Iterate until the end of the list
            temp = curr.next   # Store the next node
            curr.next = prev   # Reverse the pointer of the current node
            prev = curr        # Move prev to the current node
            curr = temp        # Move to the next node in the original list
        
        return prev            # The new head of the reversed list
