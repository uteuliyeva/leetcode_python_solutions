#Date: 010323
#Difficulty: Easy
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        N = len(strs)
        L = len(strs[0])
        res = 0
        for c in range(L):
            curr=strs[0][c]
            for r in range(N):
                if ord(strs[r][c])<ord(curr):
                    res+=1
                    break
                else:
                    curr=strs[r][c]
        return res
