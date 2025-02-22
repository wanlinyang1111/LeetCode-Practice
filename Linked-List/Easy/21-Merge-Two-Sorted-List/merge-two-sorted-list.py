class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dum = ListNode(-1)          # Create a dummy node to serve as the starting point
        curr = dum                  # Pointer to track the last node in the merged list

        while l1 and l2:            # Iterate as long as both lists have elements
            if l1.val >= l2.val:    # Compare values of current nodes in both lists
                curr.next = l2      # Attach the smaller node (l2 in this case) to the merged list
                l2 = l2.next        # Move l2 to the next node
            else:
                curr.next = l1      # Attach the smaller node (l1 in this case) to the merged list
                l1 = l1.next        # Move l1 to the next node
            curr = curr.next        # Move the current pointer forward in the merged list
        
        if not l1:                  # If l1 is exhausted, attach the remaining part of l2
            curr.next = l2

        if not l2:                  # If l2 is exhausted, attach the remaining part of l1
            curr.next = l1
        
        return dum.next             # Return the merged linked list, skipping the dummy node
