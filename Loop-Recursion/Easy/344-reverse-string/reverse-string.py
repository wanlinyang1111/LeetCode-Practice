class Solution:
    def reverseString(self, s: List[str]) -> None:
      
        def reverse(l, r, s):               # Recursive function to swap characters from both ends
            if l >= r:                      # Base case: Stop recursion when left index meets or crosses right index
                return reverse
            else:
                s[l], s[r] = s[r], s[l]     # Swap characters at left and right indices
            reverse(l + 1, r - 1, s)        # Recursive call moving towards the center
        
        return reverse(0, len(s) - 1, s)    # Initial call with full range of indices
