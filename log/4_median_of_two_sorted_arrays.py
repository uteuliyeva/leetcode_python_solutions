#Date: 031422
#Difficulty: Hard
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        MAX_NUMBER=float('inf')
        MIN_NUMBER=float('-inf')
        m=len(nums1)
        n=len(nums2)
        odd=(m+n)%2

        lo=0
        hi=m

        while lo<=hi:
            partition1=(lo+hi)//2
            partition2=(m+n)//2-partition1

            x1=nums1[partition1-1] if partition1!=0 else MIN_NUMBER
            x2=nums1[partition1] if partition1!=m else MAX_NUMBER
            y1=nums2[partition2-1] if partition2!=0 else MIN_NUMBER
            y2=nums2[partition2] if partition2!=n else MAX_NUMBER

            if x1<=y2 and y1<=x2:
                if odd:
                    return min(x2,y2)
                return (max(x1,y1)+min(x2,y2))/2.0
            elif x1>y2:
                hi=partition1-1
            else:
                lo=partition1+1
