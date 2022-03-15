#Date: 031522
#Difficulty: Easy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #take care of edge cases
        write=m+n-1
        i,j=m-1,n-1
        while i>=0 and j>=0:
            if nums2[j]>=nums1[i]:
                nums1[write]=nums2[j]
                j-=1
            else:
                nums1[write]=nums1[i]
                i-=1
            write-=1
        nums1[:j+1]=nums2[:j+1]
