#Date: 031722
#Difficulty: Easy
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i=0
        while i<len(arr)-1 and arr[i]<arr[i+1]:
            i+=1
        if i==0 or i==len(arr)-1:
            return False
        while i<len(arr)-1 and arr[i]>arr[i+1]:
            i+=1
        return i==len(arr)-1
