'''
n is number of employees

headID is where the signal starts

start at


'''

class node():
    def __init__(self, val, id, reports=[]):
        self.val = val
        self.reports = reports
        self.id = id
        self.path = self.val

    def __str__(self):
        rep = []
        for report in self.reports:
            rep.append(report.id)
        return "id: {} val: {} path: {} reports: {}".format(self.id, self.val, self.path, rep)


class Solution:

    def numOfMinutes(self, n, headID, manager, informTime): # This works
        d = {} # Lookup table
        ans = 0

        for i in range(len(informTime)):
            informTime[i] = node(informTime[i], i, [])


        for i in range(len(manager)):
            if manager[i] != -1:
                tmp = informTime[manager[i]]
                tmp.reports.append(informTime[i])

        tmp = [informTime[headID]]


        while True:

            if len(tmp) == 0:
                break

            tmp2 = []
            for element in tmp:
                reports = element.reports

                if reports == []:
                    ans = max(element.path, ans)

                elif reports != []:

                    for report in reports:
                        report.path = element.path + report.val

                    tmp2 += reports

            tmp = tmp2

        return ans



    def numOfMinutes_1(self, n, headID, manager, informTime):
        ans = informTime[headID]
        d = {}
        dI = {}

        # Create reverse look-up table
        for i in range(len(manager)):
            try:
                d[manager[i]].append(i)

            except:
                d[manager[i]] = [i]

        # print(d)


        try:
            tmp = d[headID]

        except:
            print("hi")
            return 0


        while True:

            tmp2 = []
            dI = {}
            for i in range(len(tmp)):
                try:
                    dI[informTime[tmp[i]]]
                except:
                    dI[informTime[tmp[i]]] = True
                    ans += informTime[tmp[i]]

                # print(tmp[i])
                # print("time: {}".format(informTime[tmp[i]]))


                try:
                    tmp2 += d[tmp[i]]

                except:
                    continue

            tmp = tmp2

            # print("tmp: {}".format(tmp))

            if tmp2 == []:
                break

        return ans


if __name__ == '__main__':
    s = Solution()

    tests = [
        [1,0,[-1],[0], 0],
        [6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0], 1],
        [7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1], 21],
        [4, 2, [3,3,-1,2], [0,0,162,914], 3],
        [15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0], 1076]
    ]

    i = 0
    for test in tests:
        if s.numOfMinutes(test[0], test[1], test[2], test[3]) == test[4]:
            print("[passed test {}]".format(i))

        else:
            print("[failed test {}]".format(i))

        # if s.numOfMinutes(test[0], test[1], test[2], test[3]) != test[4]:
        #     print("[passed test {}]".format(i))

        i += 1
        # print(s.numOfMinutes(test[0], test[1], test[2], test[3]))
