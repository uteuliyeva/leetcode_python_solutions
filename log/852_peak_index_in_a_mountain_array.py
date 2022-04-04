#Date: 040422
#Difficulty: Easy
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid+1]>arr[mid]:
                left=mid
            else:
                right=mid
