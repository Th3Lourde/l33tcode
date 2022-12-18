class TrieNode:
    def __init__(self, val, children, isEnd):
        self.val = val
        self.children = children
        self.isEnd = isEnd

    def __repr__(self):
        if self.isEnd:
            return "({}:{})-->{}".format(self.val, "t", self.children)

        return "({}:{})-->{}".format(self.val, "f", self.children)


class Trie:
    def __init__(self):
        self.root = TrieNode("", [], False)

    def insert(self, word):
        node = self.root
        n = len(word)

        for idx, chr in enumerate(word):
            if len(node.children) == 0:
                newNode = TrieNode(chr, [], False)

                if idx == n-1:
                    newNode.isEnd = True

                node.children.append(newNode)

                node = newNode

            else:
                found = False

                for child in node.children:
                    if child.val == chr:
                        found = True

                        if idx == n-1:
                            child.isEnd = True

                        node = child
                        break

                if not found:
                    newNode = TrieNode(chr, [], False)

                    if idx == n-1:
                        newNode.isEnd = True

                    node.children.append(newNode)

                    node = newNode

    def nodeSearch(self, word):
        node = self.root
        n = len(word)
        idx = 0
        found = True

        while found:
            found = False

            # print("(t,n,c): ({},{},{})".format(word[idx], node.val, node.children))

            for child in node.children:
                if child.val == word[idx]:
                    # print(child.val)
                    found = True

                    if idx == n-1:
                        return child

                    node = child
                    idx += 1
                    break

        return None

    def search(self, word):
        node = self.nodeSearch(word)

        if not node:
            # print("A")
            return False

        return node.isEnd

    def startsWith(self, prefix):
        node = self.nodeSearch(prefix)

        if not node:
            return False

        return True



t = Trie()
t.insert("nemathelminth")
t.insert("entracte")

t.root.children

t.startsWith("nemathelminth")
t.search("nemathelminth")
