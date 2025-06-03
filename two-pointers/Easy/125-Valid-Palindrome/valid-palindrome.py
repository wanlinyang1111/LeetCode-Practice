class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        test = []  # store only alphanumeric characters in lowercase

        for char in s:  
            if char.isalnum():  # check if character is alphanumeric
                test.append(char.lower())  # convert to lowercase and store

        left, right = 0, len(test) - 1  # initialize two pointers

        while left < right:  # continue checking while left < right
            if test[left] != test[right]:  # if characters don't match, it's not a palindrome
                return False
            left += 1  # move left pointer to the right
            right -= 1  # move right pointer to the left

        return True  # if all characters matched, it's a palindrome
