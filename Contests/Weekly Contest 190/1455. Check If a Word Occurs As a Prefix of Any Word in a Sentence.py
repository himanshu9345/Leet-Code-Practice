class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        count = 0
        for i in sentence.split(" "):
            ans = i.find(searchWord)
            if ans == 0:
                return count+1
            count += 1
        return -1
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        