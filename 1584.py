'''
Have a list of points that need connections.

For each point that needs a connection, connect
it to the nearest point. Repeat for all points.

Skip points that are already connected

So have a dict[(x,y)] = set({(x,y)})

So the keys are the points (all points are distinct)
Loop through all points, skip points that we already
have connections to, connect to the closest point.

Connect to the closest point that isn't in the group (uf)

How about we create a bunch of node objects,

Maybe it would be better to have a set, where the id of the group
is the index. The set contains the positions of the nodes.

For a given node, loop through all nodes not in the current group,
and connect to the closest one.

It is true that the number of groups must go to zero, but it isn't
true that every node must have the same number of connections.

Thus, every iteration should describe a group connecting to a node
of another group of least cost.

So how about this:
- Find the group with the least amount of nodes
- Find the min cost connection that should be made, make it
- Merge the smallest node group into the larger node group
- Continue until there is only one node group left
'''

class Solution:
    def minCostConnectPoints(self, points):
        groups = []
        cost = 0
        itrs = len(points)

        def findMinIdx(groups):
            minGroup = len(groups[0])
            minGroupIdx = 0

            for idx in range(1, len(groups)):
                if len(groups[idx]) != 0 and len(groups[idx]) < minGroup:
                    minGroups = len(groups[idx])
                    minGroupIdx = idx

            return minGroupIdx

        def lowestCostConnection(groupIdx):
            connectionCost = float('inf')
            connectionIdx = 0

            for node in groups[groupIdx]:
                for idx in range(len(groups)):
                    if idx == groupIdx:
                        continue

                    for groupNode in groups[idx]:
                        localCost = abs(node[0]-groupNode[0]) + abs(node[1]-groupNode[1])

                        if localCost < connectionCost:
                            connectionCost = localCost
                            connectionIdx = idx

            return connectionCost, connectionIdx

        for point in points:
            groups.append(set({(point[0], point[1])}))

        while len(groups) > 1:
            # print(groups)

            # Find the group with the least amount of nodes
            minGroupIdx = findMinIdx(groups)

            # print("minGroupIdx is: {}".format(minGroupIdx ))

            # Find the lowest cost connection for minGroupIdx
            connectionCost, groupIdx = lowestCostConnection(minGroupIdx)

            # print("connectionCost is: {}".format(connectionCost))

            # Add all nodes from groupIdx to minGroupIdx
            # Merge two of the groups
            groups[minGroupIdx] = groups[minGroupIdx].union(groups[groupIdx])
            del groups[groupIdx]

            cost += connectionCost

        return cost

print(Solution().minCostConnectPoints([[0,0]]))
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
