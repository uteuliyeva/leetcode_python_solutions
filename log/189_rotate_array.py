#Date: 022322
#Difficulty: Easy
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        k%=len(nums)
        def rotate_subarray(start_idx,end_idx):
            while start_idx<end_idx:
                nums[start_idx],nums[end_idx]=nums[end_idx],nums[start_idx]
                start_idx+=1
                end_idx-=1
        rotate_subarray(0,len(nums)-1)
        rotate_subarray(0,k-1)
        rotate_subarray(k,len(nums)-1)
