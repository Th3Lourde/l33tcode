'''
Design a data structure that supports
adding words and then searching for any
words that have been added.

word may contain dots '.' where dots can be matched with any letter.

1 way to do this is to use a trie
another is just to add literally every possible string that contains
a dot.

Lets do both

'''

# Add all teh dots
# Way 1, TLE
class WordDictionary_1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.alphabet = [ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        self.words = set()

    def addWord(self, word):
        words = []

        for i in range(len(word)):
            newWords = []
            if i == 0:
                if word[i] == ".":
                    for chr in self.alphabet:
                        newWords.append(chr)
                else:
                    newWords.append(word[i])

            else:
                for idx in range(len(words)):
                    if word[i] == ".":
                        for chr in self.alphabet:
                            newWords.append(words[idx]+chr)
                    else:
                        newWords.append(words[idx]+word[i])

            words = list(newWords)

        self.words = self.words.union(set(words))


    def search(self, word):
        validMatches = []

        for idx in range(len(word)):
            new_validMatches = []
            if idx == 0:
                if word[idx] == ".":
                    for chr in self.alphabet:
                        new_validMatches.append(chr)
                else:
                    new_validMatches.append(word[idx])

            else:
                for i in range(len(validMatches)):
                    if word[idx] == ".":
                        for chr in self.alphabet:
                            new_validMatches.append(validMatches[i]+chr)
                    else:
                        new_validMatches.append(validMatches[i]+word[idx])

            validMatches = new_validMatches

        return len(self.words.intersection(set(validMatches))) != 0

'''
Ok so now let's use a trie

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

    def __repr__(self):
        return "{}".format(str(self.children))

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root

        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = True

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        root = self.trie.root

        # idx of word, current trie node we are using
        def dfs(idx, node):
            if idx >= len(word):
                return node.end_node

            found = False

            for chr in node.children:
                if word[idx] == chr or word[idx] == "." or chr == ".":
                    if dfs(idx+1, node.children[chr]):
                        found = True
                        break

            return found

        return dfs(0, root)


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

wd.search("pad") # False
wd.search("bad")
wd.search("mad")
wd.search("zad")
wd.search(".ad")
wd.search("b..")



wd.addWord("foo")
wd.addWord("foobar")
wd.search("foo")
wd.search("zed")
wd.addWord("zed")
wd.search("zed")
wd.search("zad")

# print(wd.words)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
