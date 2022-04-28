class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return root

        val_to_node = {}

        def dfs(node):
            val_to_node[node.val] = node

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)

        keys = list(val_to_node.keys())

        keys.sort()

        # print(keys)
        # print(val_to_node)
        # return

        val_to_node[keys[0]].left = val_to_node[keys[-1]]

        for idx in range(1, len(keys)):
            cur = keys[idx]
            prev = keys[idx-1]


            # keys[idx].left = keys[idx-1]
            val_to_node[cur].left = val_to_node[prev]

            # keys[idx-1].right = keys[idx]
            val_to_node[prev].right = val_to_node[cur]

        val_to_node[keys[-1]].right = val_to_node[keys[0]]

        return val_to_node[keys[0]]


'''
0 : Node(0) .left = 3 .right = 1
1 : Node(1) .left = 0 .right = 2
2 : Node(2) .left = 1 .right = 3
3 : Node(3) .left = 2 .right = 0
'''
