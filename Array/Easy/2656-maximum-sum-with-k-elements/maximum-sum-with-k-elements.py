class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score=0    #initialize the score

        #loop k times to select k maximum values
        for num in range(k):  
            m=max(nums)    #get the current maximum
            score+=m    #add to the total score
            nums.append(m+1)    #remove the selected maximum
        return score    #return the total score
