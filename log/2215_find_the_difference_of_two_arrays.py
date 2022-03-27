#Date: 032722
#Difficulty: Easy
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1=set(nums1)
        set2=set(nums2)
        output=[[],[]]
        for n in set1:
            if n not in set2:
                output[0].append(n)

        for n in set2:
            if n not in set1:
                output[1].append(n)
        return output
