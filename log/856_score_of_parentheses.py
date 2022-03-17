#Date: 031722
#Difficulty: Medium
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for p in s:
            if p=="(":
                stack.append(0)
            elif stack[-1]==0:
                stack[-1]=1
            else:
                temp=0
                while stack[-1]!=0:
                    temp+=stack.pop()
                stack[-1]=2*temp
        return sum(stack)
