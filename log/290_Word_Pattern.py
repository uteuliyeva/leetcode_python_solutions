#Date: 010123
#Difficulty: Easy
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        letterToWord={}
        wordToLetter={}
        s=s.split(" ")
        if len(pattern)!=len(s):
            return False
        for i in range(len(s)):
            if pattern[i] not in letterToWord and s[i] not in wordToLetter:
                letterToWord[pattern[i]]=s[i]
                wordToLetter[s[i]]=pattern[i]
            elif letterToWord.get(pattern[i],None)!=s[i] or wordToLetter.get(s[i],None)!=pattern[i]:
                return False
        return True
