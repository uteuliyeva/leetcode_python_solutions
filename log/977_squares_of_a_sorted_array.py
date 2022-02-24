#Date: 022422
#Difficulty: Easy
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares=[None]*len(nums)
        left=0
        right=len(nums)-1
        for i in range(len(squares)-1,-1,-1):
            if nums[left]**2<=nums[right]**2:
                squares[i]=nums[right]**2
                right-=1
            else:
                squares[i]=nums[left]**2
                left+=1
        return squares
