#Date: 031522
#Difficulty: Easy
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n_dups=0
        right=len(arr)-1
        left=0
        while left<=right:
            if left>right-n_dups:
                break
            if arr[left]==0:
                if left==right-n_dups:
                    arr[right]=0
                    right-=1
                    break
                n_dups+=1
            left+=1
        last=right-n_dups
        for i in range(last,-1,-1):
            if arr[i]==0:
                arr[i+n_dups]=0
                n_dups-=1
                arr[i+n_dups]=0
            else:
                arr[i+n_dups]=arr[i]
