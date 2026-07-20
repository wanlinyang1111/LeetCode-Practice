class Solution:
    # ----------------------------------------------------
    # Approach 1: Hash Map (Dictionary)
    # Time Complexity: O(N), Space Complexity: O(N)
    # ----------------------------------------------------
    def containsDuplicate_dict(self, nums: List[int]) -> bool:
        dic = {}  # Initialize an empty dictionary to store occurrences of numbers

        for num in nums:  # Iterate through each number in the input list
            if num not in dic:  # Check if the number is not already in the dictionary
                dic[num] = 1  # Add the number to the dictionary with a count of 1
            else:  # If the number is found again, return True indicating a duplicate
                return True
        return False  # If no duplicates were found, return False.

    # ----------------------------------------------------
    # Approach 2: Hash Set (More Pythonic & Optimized Memory)
    # Time Complexity: O(N), Space Complexity: O(N)
    # Note: Using `set` reduces memory overhead compared to `dict`
    # ----------------------------------------------------
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Use a hash set for simpler lookup and lower space overhead

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
