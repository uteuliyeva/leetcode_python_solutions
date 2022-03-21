#Date: 032122
#Difficulty: Easy
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        for n in nums:
            if n>first:
                third=second
                second=first
                first=n
            elif n<first and n>second:
                third=second
                second=n
            elif n<second and n>third:
                third=n
        if third==float('-inf'):
            return first
        return third
