#Date: 033122
#Difficulty: Medium
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=list(str(num))
        if len(s)<=1:
            return num
        for i in range(len(s)-1):
            if s[i]<s[i+1]:
                break
        idx=i+1
        for j in range(i+1,len(s)):
            if s[j]>=s[idx]:
                idx=j
        for k in range(i+1):
            if s[k]<s[idx]:
                s[k],s[idx]=s[idx],s[k]
                break
        return int("".join(s))
