#Date: 031422
#Difficulty: Easy
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_streak=0
        curr_streak=0
        for n in nums:
            if n==1:
                curr_streak+=1
                max_streak=max(max_streak,curr_streak)
            else:
                curr_streak=0
        return max_streak
