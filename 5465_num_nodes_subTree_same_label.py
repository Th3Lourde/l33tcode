'''
Ok so this is a bit trickier

The goal is, for every node in the tree, to
return the number of nodes in the sub-tree
that share the same label.

This is a bit trickier because we are given
the edges.

The UID is the number of the nodes in the
edges.

What we would like to to is to create a mapping
between UID and the label.

We would also like to create a mapping between
a UID and its edges.

We would also like to create a list of all of the
UIDs that we have. The list should be sorted lo → hi.

ans = []

for every id in the list:
    perform dfs, return the max
    number of shared nodes ← indexed priority queue

    perform dfs, create dict w/label/frequency, loop
    through all keys and return the max value

    Ok so I think this works. Let's work on
    creating everything first.


UID --> label ← Given by labels, labels[UID] == label of node
UID --> edges (their UIDS)

mapping = {}

for i in range(n):
    mapping[i] = []

for edge in edges:
    mapping[edge[0]].append(edge[1])

dfs: search for the nodes that have the same label as the node we were given.

dfs(node (UID), label)

stack = mapping[node]
targ = labels[node]
resp = 0

while stack:
    node = stack.pop()

    if node:
        if labels[node] == targ:
            resp += 1

        stack = mapping[node] + stack

How about we write an algorithm in order
to improve the mapping?

we have elements that are hot.
We would like to make the edges directed.

We are given that the node is zero.

[[0,2],[0,3],[1,2]]

hot = {0}

for ... in ...
    if [0] in hot:
        mapping[0] = mapping[1]
        hot.add(mapping[1])

    elif [1] in hot:
        mapping[1] = mapping[0]
        hot.add(mapping[0])

Let's try this out and see if it
improves our mapping.

Create normal mapping first.
Then create 2nd mapping from normal
mapping

Ok so I think that worked. Hell yea.

Our mapping could be wrong?

Step through all of the edges, make sure
at least one side is included.

Maybe that test case happened.

'''

class Solution:
    def countSubTrees(self, n, edges, labels):
        mapping = {}
        adjusted = {}

        for i in range(n):
            mapping[i] = []
            adjusted[i] = []

        for edge in edges:
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])

        hot = set({})

        stack = [0]

        while stack:

            edge = stack.pop()

            if edge not in hot:
                hot.add(edge)

                nodes = mapping[edge]

                for node in nodes:
                    if node not in hot:
                        adjusted[edge].append(node)
                        stack.insert(0, node)

        mapping = adjusted

        def get_matches(node):
            stack = mapping[node]
            targ = labels[node]
            resp = 1

            while stack:
                node = stack.pop()

                if node:
                    if labels[node] == targ:
                        resp += 1

                    stack = mapping[node] + stack

            return resp

        ans = []

        for i in range(n):
            ans.append(get_matches(i))

        return ans


if __name__ == '__main__':
    s = Solution()

    # s.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd")

    s.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed")

    s.countSubTrees(25, [[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]] , "hcheiavadwjctaortvpsflssg")



[[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],
[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]]
