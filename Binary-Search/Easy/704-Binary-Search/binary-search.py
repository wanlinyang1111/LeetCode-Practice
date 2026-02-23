class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1   # initialize the search range [left, right]

        while left <= right:           # continue searching while the range is valid
            mid = (left + right) // 2 # find the middle index

            if nums[mid] == target:   # check if middle element is the target
                return mid            # return the index if found

            elif nums[mid] < target:  # target must be in the right half
                left = mid + 1        # move left pointer to mid + 1

            else:                      # nums[mid] > target, target is in the left half
                right = mid - 1       # move right pointer to mid - 1

        return -1                     # target not found in the array
