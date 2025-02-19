class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head                        # Initialize current pointer to traverse the list
        prev = None                        # Initialize previous pointer to track the node before current

        while curr:                        # Iterate through the linked list
            if curr.val == val:            # If current node's value matches the target
                if prev:                   # If there is a previous node, update its next pointer
                    prev.next = curr.next
                else:                      # If removing the head, move head to the next node
                    head = curr.next
            else:
                prev = curr                # Move previous pointer to current node
            curr = curr.next               # Move current pointer to the next node
        
        return head                        # Return the modified linked list
