class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0                       # Start of search range
        right = len(nums) - 1         # End of search range

        while left <= right:          # Continue while the range is valid
            mid = (left + right) // 2 # Find the middle index
            if nums[mid] == target:   # Found the target
                return mid
            elif nums[mid] < target:  # Target is on the right half
                left = mid + 1
            else:                     # Target is on the left half
                right = mid - 1
        return -1                     # Target not found
