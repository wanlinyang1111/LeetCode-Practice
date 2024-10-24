class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_arr = []    # Initialize an empty list for positive numbers
        neg_arr = []    # Initialize an empty list for negative numbers

        for num in nums:    # Iterate through each number in the input list
            if num > 0:
                pos_arr.append(num)    # Append positive numbers to pos_arr
            else:
                neg_arr.append(num)    # Append negative numbers to neg_arr

        ans_arr = []    # Initialize an empty list for the final rearranged array

        for i in range(len(pos_arr)):    # Loop through the range of the length of pos_arr
            ans_arr.append(pos_arr[i])    # Append the positive number at index i
            ans_arr.append(neg_arr[i])    # Append the negative number at index i
        
        return ans_arr    # Return the final rearranged array
