#Date: 022522
#Difficulty: Easy
class Solution(object):
    def moveZeroes(self, nums):
        write=0
        for read in range(len(nums)):
            if nums[read]!=0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
