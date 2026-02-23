class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Initialize total score
        score = 0
        # Find the maximum value in the list
        m = max(nums)
        # Perform the loop k times
        for i in range(k):
            score += m  # Add the maximum value to the score
            m += 1      # Increment the maximum value by 1
        # Return the total score
        return score
