class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
       
        score=0                    # Initialize the score
                                    # Loop k times to select k maximum values
        for num in range(k):  
            m=max(nums)             # Get the current maximum
            score+=m                # Add to the total score
            nums.append(m+1)        # Remove the selected maximum
        return score                # Return the total score
