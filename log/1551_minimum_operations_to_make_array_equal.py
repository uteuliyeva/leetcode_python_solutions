#Date: 031922
#Difficulty: Medium
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=n-1
        result=0
        while i>0:
            result+=i
            i-=2
        return result
