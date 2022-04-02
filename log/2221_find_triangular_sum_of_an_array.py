#Date: 040222
#Difficulty: Medium
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def generatePascalRow(n):
            prev=1
            row=[1]
            for i in range(1,n):
                curr=(row[-1]*(n-i))//i
                row.append(curr)
            return row
        row=generatePascalRow(len(nums))
        return sum(map(lambda x,y: x*y ,row,nums))%10
