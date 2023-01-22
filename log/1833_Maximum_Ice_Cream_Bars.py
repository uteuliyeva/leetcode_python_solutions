#Date: 010623
#Difficulty: Medium
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        res=0
        for i in range(len(costs)):
            if costs[i]>coins:
                return res
            res+=1
            coins-=costs[i]
        return res
