#Date: 032122
#Difficulty: Easy
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            idx=abs(n)-1
            if nums[idx]>0:
                nums[idx]*=-1
        result=[]
        for n in range(len(nums)):
            if nums[n]>0:
                result.append(n+1)
        return result
