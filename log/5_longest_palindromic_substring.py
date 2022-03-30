#Date: 033122
#Difficulty: Medium
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        start=end=0
        for i in range(len(s)):
            length1=self.expandFromMiddle(s,i,i)
            length2=self.expandFromMiddle(s,i,i+1)
            maxLength=max(length1,length2)
            if maxLength>end-start+1:
                start=i-(maxLength-1)//2
                end=i+maxLength//2
        return s[start:end+1]
    def expandFromMiddle(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
