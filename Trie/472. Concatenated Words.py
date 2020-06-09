class Node(object):
    def __init__(self):
        self.child = {}
        self.end = False
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        if not words:
            return words
        root = Node()
        for i in words:
            node  = root
            for k in i:
                if k not in node.child:
                    node.child[k] = Node()
                node = node.child[k]
            node.end = True
        res = []
        head = root
        def helper(word, end, found, root):
            # print word, end, found, root.child, root.end
            if not word:
                if end and found>=1:
                    return True
                return False
            
            isTrue = False
            start = word[0]
            
            if start not in root.child:
                if start in head.child and end:
                        return helper(word[1:], head.child[start].end, found + 1, head.child[start])
                return False
            else:
                if end:
                    if start in head.child:
                        isTrue = isTrue or helper(word[1:], head.child[start].end, found + 1, head.child[start])
                isTrue = isTrue or helper(word[1:], root.child[start].end, found, root.child[start])

            return isTrue
                
            
        
        for i in words:
            if i !="" and i[0] in root.child:
                if helper(i[1:], root.child[i[0]].end, 0, root.child[i[0]]):
                    res.append(i)
        
        return res
                
        
        """
        :type words: List[str]
        :rtype: List[str]
        """
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        seen = set(words)
        def helper(word, dict1):
            if word in dict1:
                return True
            for i in range(len(word)):
                if word[i:] in dict1 and helper(word[:i], dict1):
                    return True
            
            return False
        res = []
        for i in words:
            seen.remove(i)
            if helper(i, seen):
                res.append(i)
            seen.add(i)
        return res