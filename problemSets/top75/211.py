from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def __repr__(self):
        return "({}|{}|{})".format(self.chr, self.isWord, self.children)

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for chr in word:
            node = node.children.setdefault(chr, TrieNode())

        node.isWord = True

    def search(self, word):
        n = len(word)
        def dfs(node, idx):
            if idx == n:
                return node.isWord

            if word[idx] == ".":
                for child in node.children:
                    if dfs(node.children[child], idx+1):
                        return True

            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx+1)

            return False

        return dfs(self.root, 0)


wd = WordDictionary()

wd.addWord("a")
wd.search(".")

wd.addWord("bad")
wd.addWord("baf")
wd.addWord("ba")
wd.addWord("dad")
wd.addWord("mad")

wd.search("pad")
wd.search(".ad")
wd.search("mad")
wd.search("bad")
wd.search("b..")

wd.nodes
