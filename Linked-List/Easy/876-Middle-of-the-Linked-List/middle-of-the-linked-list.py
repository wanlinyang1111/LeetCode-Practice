class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head         # Initialize both slow and fast pointers at the head

        while fast and fast.next:  # Continue while fast and fast.next exist
            fast = fast.next.next  # Move fast pointer two steps ahead
            slow = slow.next       # Move slow pointer one step ahead
        
        return slow                # When fast reaches the end, slow is at the middle node
