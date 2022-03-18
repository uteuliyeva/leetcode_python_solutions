#Date: 031822
#Difficulty: Easy
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        write=0
        for read in range(len(nums)):
            if nums[read]%2==0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
        return nums
