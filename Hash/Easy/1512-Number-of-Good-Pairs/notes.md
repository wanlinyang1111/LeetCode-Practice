# Notes for Problem number 1512 -  Number of Good Pairs

Link: https://leetcode.com/problems/number-of-good-pairs/

## Key Concepts
- **The key concept of this problem is to count the number of "good pairs"** where `nums[i] == nums[j]` and `i < j`. Using a dictionary helps track the frequency of each number as we iterate through the list, allowing us to calculate pairs efficiently.

## 🛠️ Common Errors and How to Avoid Them

### 1. Incrementing `dic[i]` in the Correct Order:
- **Error**: Updating `dic[i]` at the wrong point in the logic.
- **Reason**: Changing `dic[i]` too early can impact the count of good pairs in the next line, leading to incorrect results.
- **How to Avoid**: Ensure that `gp += dic[num]` executes before incrementing `dic[num]`. This way, you correctly count pairs before updating the frequency.

### 2. Initializing Variables to Match the Problem Requirements:
- **Error**: Not aligning the initial variables or function purpose with the problem requirements.
- **Reason**: Starting with variables or a setup that doesn’t match the goal of counting pairs can lead to unintended logic errors.
- **How to Avoid**: Carefully consider the purpose of each variable and how it will help count "good pairs." Set `gp` to 0 to count pairs, and use `dic` as a dictionary to track occurrences of each number.

### 3. Using the Correct Bracket Type for `dic`:
- **Error**: Using square brackets `[]` instead of curly braces `{}` when initializing `dic`.
- **Reason**: Square brackets initialize a list, not a dictionary, which results in attribute errors when trying to count values.
- **How to Avoid**: Use curly braces `{}` when creating `dic` to ensure it’s initialized as a dictionary, allowing you to map numbers to their counts.
