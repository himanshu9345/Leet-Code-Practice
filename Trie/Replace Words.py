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
        char_list = []
        for c in prefix:
            if c not in node.dict1 or node.isword:
                return "".join(char_list), node.isword
            else:
                char_list.append(c)
                node = node.dict1[c]
        return "".join(char_list), node.isword
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """


class Solution(object):
    def replaceWords(self, dict, sentence):
        trie = Trie()
        for word in dict:
            trie.insert(word)

        sen = sentence.split()
        sen1 = []
        for word in sen:
            new1, bo = trie.startsWith(word)
            if bo:
                sen1.append(new1)
            else:
                sen1.append(word)
        return " ".join(sen1)
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
