#Date: 030122
#Difficulty: Easy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement={}
        for i,n in enumerate(nums):
            if n in complement:
                return [complement[n],i]
            complement[target-n]=i
