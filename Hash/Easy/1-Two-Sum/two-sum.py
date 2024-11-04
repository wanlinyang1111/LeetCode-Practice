class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}        　                   # Dictionary to store numbers and their indices
        
        for index, num in enumerate(nums):            # Loop through nums with both index and value
            remain = target - num                     # Calculate the required complement
            
            if remain in num_to_index:                # Check if complement exists in the dictionary
                return [index, num_to_index[remain]]  # Return current index and complement's index
            else:
                num_to_index[num] = index             # Store current number and its index
