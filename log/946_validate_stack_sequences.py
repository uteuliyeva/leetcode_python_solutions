#Date: 031622
#Difficulty: Medium
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        i=0
        for n in popped:
            found=False
            if stack and n==stack[-1]:
                stack.pop()
                found=True
            else:
                while i<len(pushed):
                    if pushed[i]!=n:
                        stack.append(pushed[i])
                        i+=1
                    else:
                        found=True
                        i+=1
                        break
            if not found:
                return False
        return True
