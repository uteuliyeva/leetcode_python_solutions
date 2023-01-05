#Date: 050123
#Difficulty: Medium
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr = sorted(points)
        res=0
        curr=arr[0]
        for i in range(1,len(arr)):
            if arr[i][0]>curr[1]:
                res+=1
                curr=arr[i]
            curr=[arr[i][0], min(curr[1],arr[i][1])]
        res+=1
        return res
