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

class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        self.rows = len(board)
        self.cols = len(board[0])
        res, trie = [], Trie()

        for word in words:
            trie.insert(word)

        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, trie.root, r, c, "", res)

        return res

    def dfs(self, board, node, r, c, path, res):
        if self.num_words == 0: return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]): return
        tmp = board[r][c]

        if tmp not in node.children: return

        board[r][c] = "#"

        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            self.dfs(board, node.children[tmp], nr, nc, path+tmp, res)

        board[r][c] = tmp

# Correct, too slow use trie
class Solution:
    def findWords(self, board, words):
        chrToSqr = {}
        rows = len(board)
        cols = len(board[0])

        for word in words:
            chrToSqr[word[0]] = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in chrToSqr:
                    chrToSqr[board[row][col]].add((row, col))

        # print(chrToSqr)

        def dfs(r, c, idx, word, visited):
            # print("board[{}][{}] --> {}, idx: {}, word: {}".format(r,c,board[r][c],idx,word))
            if idx == len(word):
                return True

            if board[r][c] != word[idx]:
                return False

            if idx == len(word)-1:
                return True

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((r,c))
                    if dfs(nr, nc, idx+1, word, visited):
                        return True
                    visited.remove((r,c))

            return False

        wordsOnBoard = []

        for word in words:
            for r,c in chrToSqr[word[0]]:
                if len(word) == 1 or dfs(r, c, 0, word, set()):
                    wordsOnBoard.append(word)
                    break

        return wordsOnBoard


print(Solution().findWords([["a","a"]], ["aa"]))

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["a"]))
print(Solution().findWords([["a"]], ["a"]))

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))

print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","oathi","oathf","oathk","oate"]))
