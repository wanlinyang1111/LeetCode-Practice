class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp = 0                   # Set 'gp' to track the count of good pairs.
        dic = {}                 # Initialize 'dic' as an empty dictionary to count occurrences of each number.

        for num in nums:         # Loop through each number in 'nums'.
            if num in dic:       # If 'num' is already in 'dic', it means we found pairs.
                gp += dic[num]   # Add the count in 'dic' to 'gp' for new pairs.
                dic[num] += 1    # Increase 'num' count in 'dic'.
            else:
                dic[num] = 1     # If 'num' is new, set its count to 1.
                
        return gp                # Return the total count of good pairs.
