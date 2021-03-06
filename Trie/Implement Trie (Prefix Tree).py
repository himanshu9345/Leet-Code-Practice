class Node(object):
    def __init__(self):
        self.dict1 = {}
        self.isword = False


class Trie(object):

    def __init__(self):
        self.root = Node()
        """
        Initialize your data structure here.
        """

    def insert(self, word):
        node = self.root
        for c in word:
            if c in node.dict1:
                node = node.dict1[c]
            else:
                node.dict1[c] = Node()
                node = node.dict1[c]
        node.isword = True
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.dict1:
                return False
            else:
                node = node.dict1[c]

        return node.isword
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.dict1:
                return False
            else:
                node = node.dict1[c]
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)