#Date: 040722
#Difficulty: Easy
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            coins=mid*(mid+1)//2
            if coins==n:
                return mid
            elif n<coins:
                right=mid-1
            else:
                left=mid+1
        return right
