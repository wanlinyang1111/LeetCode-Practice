class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}                                  # Create an empty dictionary to count characters in string s
        dic_t = {}                                  # Create an empty dictionary to count characters in string t

        if len(s) != len(t):                        # Check if the lengths of both strings are equal
            return False                            # If lengths differ, they cannot be anagrams

        for i in s:                                 # Iterate through each character in string s
            if i not in dic_s:                      # If character is not in dic_s
                dic_s[i] = 1                        # Initialize count for this character
            else:
                dic_s[i] += 1                       # Increment count for this character

        for i in t:                                 # Iterate through each character in string t
            if i not in dic_t:                      # If character is not in dic_t
                dic_t[i] = 1                        # Initialize count for this character
            else:
                dic_t[i] += 1                       # Increment count for this character     

        for i in s:                                 # Iterate through each character in string s again
            if i not in t or dic_s[i] != dic_t[i]:  # Check if the character is not in t or counts don't match
                return False                        # If either condition is true, return False
        return True                                 # If all conditions are met, return True
