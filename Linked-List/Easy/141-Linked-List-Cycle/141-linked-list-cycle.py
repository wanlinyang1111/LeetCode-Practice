class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head         # Initialize two pointers, fast and slow, both starting at head

        while fast and fast.next:  # Ensure fast pointer and its next node are not None
            fast = fast.next.next  # Move fast pointer two steps forward
            slow = slow.next       # Move slow pointer one step forward
            if fast == slow:       # If fast and slow pointers meet, there is a cycle
                return True
        
        return False               # If the loop exits, no cycle was found
