class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dum = ListNode(-1)              # Create a dummy node to simplify merging, avoiding special cases for the first node
        curr = dum                      # Pointer to track the merged list

        while l1 and l2:                # Iterate while both lists have remaining nodes
            if l1.val <= l2.val:        # If l1's value is smaller or equal, attach l1
                curr.next = l1  
                l1 = l1.next            # Move l1 forward
            else:                       # Otherwise, attach l2
                curr.next = l2  
                l2 = l2.next            # Move l2 forward
            curr = curr.next            # Move the pointer forward
        
        if not l1:                      # If l1 is exhausted, attach the remaining l2
            curr.next = l2  

        if not l2:                      # If l2 is exhausted, attach the remaining l1
            curr.next = l1  
        
        return dum.next                  # Return the merged list starting from the first real node
