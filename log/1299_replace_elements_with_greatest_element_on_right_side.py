#Date: 031822
#Difficulty: Easy
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        prev_max=-1
        for i in range(len(arr)-1,-1,-1):
            new_max=max(arr[i],prev_max)
            arr[i]=prev_max
            prev_max=new_max
        return arr
