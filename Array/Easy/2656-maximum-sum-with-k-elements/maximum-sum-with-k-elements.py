class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score=0

        for num in range(k):  
            m=max(nums)
            score+=m
            nums.append(m+1)
        return score
