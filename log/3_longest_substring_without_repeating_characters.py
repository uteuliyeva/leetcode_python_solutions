#Date: 022822
#Difficulty: Medium
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        left=0
        length=0
        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]]=right
            else:
                left=max(seen[s[right]]+1,left)
                seen[s[right]]=right
            length=max(length,right-left+1)
        return length
