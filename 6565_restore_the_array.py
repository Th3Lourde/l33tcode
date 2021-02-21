class Solution:
    def restoreArray(self, adjacentPairs):

        for i in range(len(adjacentPairs)):
            pair = adjacentPairs[i]

            if pair[0] > pair[1]:
                t = pair[0]
                pair[0] = pair[1]
                pair[1] = t

            adjacentPairs[i] = pair

        # adjacentPairs.sort(key=lambda x: x[0])

        print(adjacentPairs)

        l = {}
        lSet = set()
        rSet = set()

        for pair in adjacentPairs:
            # l[pair[0]] = pair[1]
            # r[pair[1]] = pair[0]

            if pair[0] in l:
                l[pair[0]].append(pair[1])
            else:
                l[pair[0]] = [pair[1]]

            if pair[1] in l:
                l[pair[1]].append(pair[0])
            else:
                l[pair[1]] = [pair[0]]


            lSet.add(pair[0])
            rSet.add(pair[1])

        print(l)
        print(lSet)
        print(rSet)

        for k in l:
            if len(l[k]) == 1:
                endpoint = k
                break



        # endpoint = rSet.union(lSet) - lSet.intersection(rSet)
        # endpointList = list(rSet.union(lSet) - rSet)
        #
        # endpoint = endpointList[0]

        print(endpoint)

        ans = [endpoint]
        seen = set({endpoint})

        print("ans: {}".format(ans))
        print("seen: {}".format(seen))

        n = endpoint

        while True:

            opts = l[n]

            for opt in opts:
                if opt not in seen:
                    n = opt

            if n == ans[-1]:
                break

            ans.append(n)
            seen.add(n)

        return ans





if __name__ == '__main__':
    s = Solution()

    print(s.restoreArray([[2,1],[3,4],[3,2]]))

    print(s.restoreArray([[4,-10],[-1,3],[4,-3],[-3,3]]))
