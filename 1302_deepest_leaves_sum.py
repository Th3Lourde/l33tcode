'''
itr via level order and return sum

have a lcl var that keeps track of the current lvl

each node has the level as well as the value

bfs

ans = 0
lvl = 0

(lvl, val)
(0, 1)

if lvl == lvl:
    ans += val

else:
    lvl = lvl
    ans = val


return ans

Ok, so only += ans if we are a leaf



'''

class Solution:


    # Redo
    def deepestLeavesSum(self, root):
        ans = 0
        lvl = 0

        q = [(0, root)]

        while q:
            node = q.pop()

            if node[1].left and node[1].right:
                q.insert(0, (node[0]+1, node[1].left))
                q.insert(0, (node[0]+1, node[1].right))

            elif node[1].left:
                q.insert(0, (node[0]+1, node[1].left))

            elif node[1].right:
                q.insert(0, (node[0]+1, node[1].right))

            else:

                if node[0] == lvl:
                    ans += node[1].val

                # elif node[0] > lvl:
                else: # Do I need the elif?
                    lvl = node[0]
                    ans = node[1].val

        return ans


    def deepestLeavesSum_correct(self, root): # This works, is slow

        d = {}
        q = [ [root, 0] ]

        h = 0

        while q:
            node = q.pop()

            if node[0]:
                h = max(h, node[1])

                # add val to dict
                try:
                    d[node[1]] += node[0].val

                except:
                    d[node[1]] = node[0].val

                # continue traversal
                q = [ [node[0].right, node[1]+1],  [node[0].left, node[1]+1]  ] + q


        return d[h]
