#Date: 040622
#Difficulty: Easy
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left=1
        right=num
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right=mid-1
            else:
                left=mid+1
        return False