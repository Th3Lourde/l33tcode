
import collections

class Solution:
    def countSubTrees(self, n, edges, labels):
            # Use the UID (int)
        def dfs(node, parent):
            cntr = collections.Counter()

            for child in tree[node]:
                if child == parent: continue
                cntr += dfs(child, node)

            cntr[labels[node]] += 1
            result[node] = cntr[labels[node]]
            return cntr

        # Create mapping for tree
        tree = collections.defaultdict(list)

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        result = [0]*n
        dfs(0, None)
        return result



if __name__ == '__main__':
    s = Solution()

    print(s.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"))
