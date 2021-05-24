from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

    def __repr__(self):
        return "{}".format(str(self.children))

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root

        for chr in word:
            root = root.children.setdefault(chr, TrieNode())

        root.endNode = True

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.addWord(word)

    def search(self, word):
        node = self.trie.root

        q = deque()
        q.append((node, 0))

        while q:
            trieNode, idx = q.popleft()

            if idx >= len(word):
                if trieNode.endNode:
                    return True

                continue

            # print(word[idx])
            #
            # print(trieNode.children)

            nextChr = word[idx]

            if word[idx] == ".":
                nextChr = "abcdefghijklmnopqrstuvwxyz"

            for chr in list(nextChr):
                if chr not in trieNode.children or trieNode.endNode:
                    continue

                q.append((trieNode.children[chr], idx+1))

        return False












# too slow
class WordDictionary_1:

    def __init__(self):
        self.words = set()

    def addWord(self, word):
        self.words.add(word)

    def search(self, word):
        q = deque()
        queries = []

        q.append(("", 0))

        while q:
            query, idx = q.popleft()

            if idx >= len(word):
                queries.append(query)
                continue

            if word[idx] != ".":
                q.append((query+word[idx], idx+1))
            else:
                for chr in "abcdefghijklmnopqrstuvwxyz":
                    q.append((query+chr, idx+1))

        for query in queries:
            if query in self.words:
                return True

        return False


wd = WordDictionary()

wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
wd.search("pad") # False
wd.search("bad") # True
wd.search(".ad") # True
wd.search("b..") # True
wd.search("...") # True
wd.search("....") # False
