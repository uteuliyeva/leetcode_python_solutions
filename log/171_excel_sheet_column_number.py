#Date: 032822
#Difficulty: Easy
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnNum=0
        for i in range(len(columnTitle)):
            columnNum*=26
            columnNum+=ord(columnTitle[i])-ord('A')+1
        return columnNum
