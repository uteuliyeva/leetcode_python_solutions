#Date: 032722
#Difficulty: Medium
class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        deletions=0
        for i in range(len(nums)):
            if idx%2==0 and i!=len(nums)-1 and nums[i]==nums[i+1]:
                deletions+=1
            else:
                idx+=1
        return deletions+(len(nums)-deletions)%2
