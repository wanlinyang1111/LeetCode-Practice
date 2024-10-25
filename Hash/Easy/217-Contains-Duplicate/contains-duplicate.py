class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty dictionary to store occurrences of numbers
        dic = {}  

        # Iterate through each number in the input list
        for num in nums:
            # Check if the number is not already in the dictionary
            if num not in dic:
                # Add the number to the dictionary with a count of 1
                dic[num] = 1  
            else:
                # If the number is found again, return True indicating a duplicate
                return True  
        
        # If no duplicates were found, return False
        return False 
