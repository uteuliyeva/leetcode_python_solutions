#Date: 040222
#Difficulty: Medium
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=[None]*len(s)
        right=[None]*len(s)
        n_1=0
        n_0=0
        for i in range(len(s)):
            if s[i]=="0":
                n_0+=1
                left[i]=n_1
            else:
                n_1+=1
                left[i]=n_0
        n_1=0
        n_0=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                n_0+=1
                right[i]=n_1
            else:
                n_1+=1
                right[i]=n_0
        return sum(map(lambda x,y: x*y ,left,right))
