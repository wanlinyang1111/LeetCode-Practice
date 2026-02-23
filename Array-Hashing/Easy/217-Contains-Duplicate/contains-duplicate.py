class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic = {}              　# Initialize an empty dictionary to store occurrences of numbers

        for num in nums:        # Iterate through each number in the input list
            if num not in dic:  # Check if the number is not already in the dictionary
                dic[num] = 1    # Add the number to the dictionary with a count of 1  
            else:               # If the number is found again, return True indicating a duplicate
                return True  
        return False            # If no duplicates were found, return False. 
