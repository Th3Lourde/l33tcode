class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.subStrs = set()
        self.words = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        for idx in range(1, len(word)+1):
            self.subStrs.add(word[:idx])

        self.words.add(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        return word in self.words

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.subStrs

t = Trie()
t.insert("apple")
t.search("apple")
t.search("app")
t.startsWith("app")
t.insert("app")
