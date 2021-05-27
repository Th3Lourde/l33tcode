class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

    def __repr__(self):
        return "{}".format(str(self.children))

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root

        for chr in word:
            root = root.children.setdefault(chr, TrieNode())

        root.endNode = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.endNode

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False

        return dfs(self.root, 0)












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


["WordDictionary","addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
[[],["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]

wd.addWord("rune")
wd.addWord("runner")
wd.addWord("runs")
wd.addWord("add")
wd.addWord("adds")
wd.addWord("adder")
wd.addWord("addee")

wd.search("r.n") # True
wd.search("ru.n.e") # False
wd.search("add") # True
wd.search("add.") # True
wd.search("adde.") # True
wd.search(".an.")
wd.search("...s")
wd.search("....e.")
wd.search(".......")
wd.search("..n.r")

wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
wd.search("pad") # False
wd.search("bad") # True
wd.search(".ad") # True
wd.search("b..") # True
wd.search("...") # True
wd.search("....") # False
wd.search("..") # False
