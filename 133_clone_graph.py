
'''




create dict to keep track of nodes we have seen.

If node in dict: do nothing


Given a node.
if node not in dict or node in di, create a node of same value. Loop through neighbors, creating proper adj lists.
    - Create the neighbors as we go.


node not in dict:
    create node with values, iterate through neighbors, check if the neighbors are nodes. "Repeat previous process"
    add neighbors to queue
node in dict, neighbors == []
    iterate through neighbors, check if the neighbors are nodes. "Repeat previous process". If neighbors exist, don't add them to the queue.

if node in dict, neighbors != [], continue


1, [2,4]
--------
d = {1: [2,4], 2: [], 4: []}
q = [4,2]


try:
    d[1]

    for n in neighbors:
        try:
            if d[n.val]:
                q.insert(0, d[n])

        except:
            d[n.val] = Node(n.val)
            q.insert(0, d[n])

        d[node.val].neighbors.append(d[n.val])

except:

    tmp = Node(1.val)
    d[1] = tmp

    for n in neighbors:
        try:
            if d[n.val]:
                q.insert(0, d[n])

        except:
            d[n.val] = Node(n.val)
            q.insert(0, d[n])

        d[node.val].neighbors.append(d[n.val])





'''

'''
Copy of answer I wrote on LC.

       ans = node.val

        d = {}
        q = [node]

        while q:
            node = q.pop()

            try:
                if d[node.val]:
                    for n in node.neighbors:
                        try:
                            if d[n.val]:
                                d[node.val].neighbors.append(d[n.val])

                        except:
                            tmp = Node(val = n.val, neighbors = [])

                            d[n.val] = tmp
                            d[node.val].neighbors.append(d[n.val])
                            q.append(n)


            except:
                tmp = Node(val = node.val, neighbors = [])
                d[node.val] = tmp

                for n in node.neighbors:
                    try:
                        if d[n.val]:
                            d[node.val].neighbors.append(d[n.val])

                    except:
                        tmp = Node(val = n.val, neighbors = [])
                        d[n.val] = tmp
                        d[node.val].neighbors.append(d[n.val])
                        q.append(n)


        nodes = list(d.keys())

#         for n in nodes:
#             s = ".val={}".format(d[n].val)
#             neighs = []

#             for adj in d[n].neighbors:
#                 neighs.append(d[adj.val].val)

#             s = s + " .n = [{}]".format(neighs)
#             # print(neighs)
#             print(s)


        return d[ans]
'''





class Solution:
    def cloneGraph(self, node): # This works

        if not node:
            return node

        ans = node.val

        d = {}
        q = [node]

        while q:
            node = q.pop()

            try:
                if d[node.val]:
                    for n in node.neighbors:
                        try:
                            if d[n.val]:
                                d[node.val].neighbors.append(d[n.val])

                        except:
                            tmp = Node(n.val)
                            d[n.val] = tmp
                            d[node.val].neighbors.append(d[n.val])
                            q.append(n)


            except:
                tmp = Node(node.val)
                d[node.val] = tmp

                for n in node.neighbors:
                    try:
                        if d[n.val]:
                            d[node.val].neighbors.append(d[n.val])

                    except:
                        tmp = Node(n.val)
                        d[n.val] = tmp
                        d[node.val].neighbors.append(d[n.val])
                        q.append(n)



        return d[ans]
