class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def dfs(node, path, target):
            if node.val == target:
                return path + [node]

            if node.left:
                resp = dfs(node.left, path+[node], target)

                if len(resp) > 0:
                    return resp

            if node.right:
                resp = dfs(node.right, path+[node], target)

                if len(resp) > 0:
                    return resp

            return []

        pathP = dfs(root, [], p.val)
        pathQ = dfs(root, [], q.val)

        longer = pathP

        if len(pathP) < len(pathQ):
            longer = pathQ

        shorter = pathQ

        if len(shorter) > len(pathP):
            shorter = pathP

        seen = set()

        for node in shorter:
            seen.add(node.val)

        # print(seen)
        # print(longer)

        while longer:
            node = longer.pop()

            if node.val in seen:
                # perform dfs search for node
                return node

            seen.add(node.val)
