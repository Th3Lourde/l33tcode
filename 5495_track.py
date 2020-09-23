

class Solution:
    def mostVisited(self, n, rounds):
        d = {-1:-1}
        max = -1

        for i in range(1, len(rounds)):
            start = i-1
            end = i

            if rounds[start] > rounds[end]:
                itrs = [z for z in range(rounds[start]+1, n+1)] + [z for z in range(1, rounds[end]+1)]

            else:
                itrs = [z for z in range(rounds[start]+1, rounds[end]+1)]

            if i == 1:
                itrs.insert(0, rounds[start])

            for x in range(len(itrs)):
                if itrs[x] in d:
                    d[itrs[x]] += 1

                else:
                    d[itrs[x]] = 1

        popular = [0, []]

        for key in list(d.keys()):
            if d[key] > popular[0]:
                popular = [d[key], [key]]

            elif d[key] == popular[0]:
                popular[1].append(key)
                
        popular[1].sort()

        return popular[1].sort()




if __name__ == '__main__':
    s = Solution()

    print(s.mostVisited(4, [1,3,1,2]))

    print(s.mostVisited(2, [2,1,2,1,2,1,2,1,2]))

    print(s.mostVisited(7, [1,3,5,7]))
