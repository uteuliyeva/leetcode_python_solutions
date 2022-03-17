#Date: 031722
#Difficulty: Easy
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen=set()
        for i in range(len(arr)):
            if 2*arr[i] in seen or arr[i]/2.0 in seen:
                return True
            seen.add(arr[i])
        return False
