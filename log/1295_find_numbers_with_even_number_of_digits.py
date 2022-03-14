#Date: 031422
#Difficulty: Easy
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for n in nums:
            if len(str(n))%2==0:
                result+=1
        return result
