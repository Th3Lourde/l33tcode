
class Solution:
    def findMinHeightTrees(self, n, edges):
        # 1) Create dictionary that returns
        # what a given node is surrounded by
        # DONE

        if edges == []:
            return None

        self.graph = {}

        # for i in range(n):
        #     self.graph[i] = []

        for i in range(len(edges)):
            # try:
            #     self.graph[edges[i][0]].append(edges[i][1])
            #     self.graph[edges[i][1]].append(edges[i][0])
            # except:
            #     self.graph[edges[i][0]] = [edges[i][1]]
            #     self.graph[edges[i][1]] = [edges[i][0]]

            try:
                self.graph[edges[i][0]].append(edges[i][1])
            except:
                self.graph[edges[i][0]] = [edges[i][1]]

            try:
                self.graph[edges[i][1]].append(edges[i][0])
            except:
                self.graph[edges[i][1]] = [edges[i][0]]


        # 2) Find the leaf nodes
        # DONE

        self.leafs = []

        for key in self.graph:
            if len(self.graph[key]) == 1:
                self.leafs.append(key)
        #
        # print(self.leafs)

        print(self.graph)

        # 3) For each node in the graph calculate
        # the maximum height (by searching for the leaf-nodes)

        self.max = {'val': None, 'nodes': []}

        # r = self.get_dist(0, None, 0, 0)
        # print(r)
        #
        # r = self.get_dist(1, None, 0, 0)
        # print(r)

        for i in range(n):
            # i is the current node
            # TODO: Write get_dist
            r = self.get_dist(i, None, 0, 0)
            # print("Node: {}, Dist: {}".format(i, r))

        # 4) Keep track of the minimum height (and what nodes have it)
        # in a third dictionary
        # DONE

            if self.max['val'] == None:
                self.max['val'] = r
                self.max['nodes'].append(i)

            elif self.max['val'] == r:
                self.max['nodes'].append(i)

            elif self.max['val'] > r:
                self.max['val'] = r
                self.max['nodes'] = [i]

        # print(self.max)



        # 5) Figure out what the minimum height is and return the nodes
        # that have it.
        return self.max['nodes']

    def get_dist(self, current, prev, walk, max):
        n1 = self.graph[current]

        if walk == 0:
            for edge in n1:
                dist = self.get_dist(edge, current, walk+1, max)

                if dist > max:
                    max = dist

            return max

        elif walk != 0:
            # n1.remove(current)
            if len(n1) == 1:
                return walk
            else:
                for edge in n1:
                    if edge != prev:
                        dist = self.get_dist(edge, current, walk+1, max)
                        if dist > max:
                            max = dist
                return max






if __name__ == '__main__':
    s = Solution()

    # n = 4
    # edges = [[1, 0], [1, 2], [1, 3]]

    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

    print(s.findMinHeightTrees(n,edges))
