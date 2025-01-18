class Solution:
    def rearrangeArray(self, nums):
        
        # Separate positive and negative numbers
        for i in nums:
            if i > 0:
                pos_arr.append(i)
            else:
                neg_arr.append(i)

        mod_arr = []  # To store the rearranged array

        # Use enumerate to combine positive and negative numbers alternately
        for index, value in enumerate(pos_arr):
            mod_arr.append(value)           # Add the positive number
            mod_arr.append(neg_arr[index]) # Add the corresponding negative number

        return mod_arr
