#Date: 031422
#Difficulty: Hard
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        MAX_NUMBER=float('inf')
        MIN_NUMBER=float('-inf')
        n=len(nums1)
        m=len(nums2)
        odd=(m+n)%2
        left_size=(m+n)//2+(m+n)%2

        lo=0
        hi=n-1

        while lo<=hi:
            idx1=(lo+hi)//2
            idx2=left_size-idx1-2
            x1=nums1[idx1] if idx1>=0 else MIN_NUMBER
            x2=nums1[idx1+1] if idx1+1<n else MAX_NUMBER
            y1=nums2[idx2] if idx2>=0 else MIN_NUMBER
            y2=nums2[idx2+1] if idx2+1<m else MAX_NUMBER

            if x1<=y2 and y1<=x2:
                if odd:
                    return max(x1,y1)
                return (max(x1,y1)+min(x2,y2))/2.0
            elif x1>y2:
                hi=idx1-1
            else:
                lo=idx1+1
        if odd:
            return nums2[m//2]
        return (nums2[m//2-1]+nums2[m//2])/2.0
