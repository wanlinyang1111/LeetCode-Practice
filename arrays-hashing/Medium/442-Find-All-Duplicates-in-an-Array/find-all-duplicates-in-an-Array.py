class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

      ans_arr = []                            # First, I will initialize an empty array to store the answer.

      for num in nums:                        # Next, I will iterate through the `nums` array for each number. 
          index = abs(num) - 1                # I will calculate the index based on the absolute value of the number.　Using the abs function to get the index.
          if nums[index] > 0:                 # If the value at this index is greater than zero,
              nums[index] = -nums[index]      # I will mark it as negative.
          else:
              ans_arr.append(abs(num))        # Otherwise, I will append the absolute value of the number to the answer array.
      return ans_arr                          # Finally, after iterating through the entire array, I will return the answer array.

