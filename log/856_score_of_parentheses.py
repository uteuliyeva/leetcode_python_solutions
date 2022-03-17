#Date: 031722
#Difficulty: Medium
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=power=0
        for i in range(len(s)):
            if s[i]=='(':
                power+=1
            else:
                power-=1
                if s[i-1]=='(':
                    result+=2**power
        return result
