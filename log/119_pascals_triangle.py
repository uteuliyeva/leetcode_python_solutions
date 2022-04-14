#Date: 041422
#Difficulty: Easy
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for i in range(1,rowIndex+1):
            curr=(row[-1]*(rowIndex+1-i))//i
            row.append(curr)
        return row
