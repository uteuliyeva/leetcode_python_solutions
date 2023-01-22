#Date: 010423
#Difficulty: Medium
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        count=Counter(tasks)
        res=0
        for i in count.keys():
            if count[i]==1:
                return -1
            res+=(count[i]//3)
            res+=1 if count[i]%3>0 else 0
        return res
