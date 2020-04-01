
'''
Yea so I completely misunderstood this problem
watch https://www.youtube.com/watch?v=eGf-26OTI-A
if you want to get an idea of what we are actually
solving for. I currently have 3-cases that will result
in a solution. Maybe I need less. I will figure it out
in time :)

[3/29/20]
Almost done with the first version of case 1.
Currently, case 1 fails 3A3B. Need to check that
d[sortedD[0]] > d[sortedD[1]] (also that len(sortedD) > 1)
as well as the current check that I have implemented.
'''


class Solution:

    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        d = {}

        for task in tasks:
            try:
                d[task] += 1

            except:
                d[task] = 1

        sortedD = sorted(d, key=d.get, reverse=True)

        if len(sortedD) == 1:
            return (d[sortedD[0]]-1)*(n+1) + 1

        if n == 1:
            print("Case 0")
            a = sortedD[0]
            b = sortedD[1]
            ansS = ""


            while True:
                ansS += a
                ansS += b

                d[a] -= 1
                d[b] -= 1

                if d[a] == 0 and d[b] == 0:
                    sortedD.remove(a)
                    sortedD.remove(b)

                    if len(sortedD) == 0:
                        return len(ansS)

                    elif len(sortedD) == 1:
                        # we might be in trouble
                        for i in range(d[sortedD[0]]):
                            ansS += sortedD[0]+" "

                        return len(ansS)-1

                    elif len(sortedD) >= 2:
                        a = sortedD[0]
                        b = sortedD[1]


                elif d[a] == 0  and d[b] != 0:
                    sortedD.remove(a)

                    if len(sortedD) == 1:
                        for i in range(d[b]):
                            ansS += b+" "

                        return len(ansS)-1


                    elif len(sortedD) >= 2:
                        a = b
                        b = sortedD[1]

                elif d[a] != 0 and d[b] == 0:

                    sortedD.remove(b)

                    if len(sortedD) == 1:
                        for i in range(d[a]):
                            ansS += a+" "

                        return len(ansS)-2

                    elif len(sortedD) >= 2:
                        b = sortedD[1]




        # Case 1
        if (d[sortedD[0]]-1)*(n)+1 > (len(tasks)-d[sortedD[0]]) and d[sortedD[0]] > d[sortedD[1]]:
            print("Case 1")
            return (d[sortedD[0]]-1)*(n)+d[sortedD[0]]

        elif (d[sortedD[0]]-1)*(n)+1 > (len(tasks)-d[sortedD[0]]) and d[sortedD[0]] == d[sortedD[1]]:
            print("Case 2")

            print(d)
            z = 1
            i = 1
            while True:
                i += 1
                try:
                    sortedD[i]
                    if d[sortedD[i]] == d[sortedD[0]]:
                        z = i
                except:
                    # z -= 1
                    break

            # print("z: {}".format(z))

            return (d[sortedD[0]]-1)*(n)+d[sortedD[0]]+z

        else:

            if d[sortedD[0]] > d[sortedD[-1]]:
                print(d)
                print("case 3 [a]")

                ans = 0
                ansS = ""

                while True:
                    t = n
                    lead = sortedD[0]
                    i = 0
                    l = len(sortedD)

                    if len(ansS) >= n+1:
                        # Find the nearest lead
                        # closest to the end
                        # if lead is too close,
                        # add spaces as required
                        di = 0
                        z = len(ansS)-1

                        while ansS[z] != lead:

                            if z < 0:
                                print("houston, we have a problem")
                                break

                            di += 1
                            z -= 1

                        ansS += " "*(n-di)

                    while i < l:

                        if t == 0:
                            t = n
                            i = 0

                        ans += 1

                        ansS += sortedD[i]

                        d[sortedD[i]] -= 1

                        if sortedD[i] != lead:
                            t -= 1

                        if d[sortedD[i]] == 0:
                            if sortedD[i] == lead:
                                try:
                                    lead = sortedD[i+1]

                                except:
                                    # print(d)
                                    # print(ansS)
                                    return len(ansS)
                                    # return ans

                            del sortedD[i]
                            i -=1
                            l = len(sortedD)

                        i += 1

                return ans


            elif d[sortedD[0]] <= d[sortedD[-1]]:
                # print(d)
                print("case 3 [b]")
                ans = 0
                ansS = ""

                while True:
                    t = n
                    lead = sortedD[0]
                    i = 0
                    l = len(sortedD)

                    if len(ansS) >= n+1:
                        # Find the nearest lead
                        # closest to the end
                        # if lead is too close,
                        # add spaces as required
                        di = 0
                        z = len(ansS)-1

                        while ansS[z] != lead:

                            if z < 0:
                                print("houston, we have a problem")
                                break

                            di += 1
                            z -= 1

                        if len(" "*(n-di)) == 1 and ansS[0] not in ansS[len(ansS)-n-1:]:

                            tmp = ansS[0]
                            ansS = ansS[1:] + tmp
                        else:
                            ansS += " "*(n-di)

                    while i < l:

                        if t == 0:
                            t = n
                            i = 0

                        ans += 1

                        ansS += sortedD[i]

                        d[sortedD[i]] -= 1

                        if sortedD[i] != lead:
                            t -= 1

                        if d[sortedD[i]] == 0:
                            if sortedD[i] == lead:
                                try:
                                    lead = sortedD[i+1]

                                except:
                                    # print(d)
                                    # print(ansS)
                                    return len(ansS)
                                    # return ans

                            del sortedD[i]
                            i -=1
                            l = len(sortedD)

                        i += 1

                return ans





    def leastInterval1(self, tasks, n):
        if n == 0:
            return len(tasks)

        ans = [tasks[0], 1]
        d = {tasks[0]:1}

        for task in tasks:
            try:
                d[task] += 1

            except:
                d[task] = 1

            if d[task] > ans[1]:
                ans = [task, d[task]]

        return n*ans[1]





if __name__ == '__main__':
    s = Solution()

    testCases = [
        # [["C","C","D","A","A","A","B","B","B"], 2, 8],
        # [["A","A"], 2, 4],
        # [["A","B","C","D","E","A","B","C","D","E"], 4, 10],
        # [["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7, 18],
        #
        # [ ["A","A","A","A","B","B","B","B","C","C","C","C","D","D","D","D","E","F"], 4, 19],
        #
        # [["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"], 2, 52],
        #
        #
        # [["A","A","A","A","B","B","B","B","C","C","C","C","D","D","D","D","E","F"], 4, 19],
        [["A","B"], 1, 2]

    ]


    # print(s.leastInterval(["A","A","A","B","B","B"], 50))


    # print(s.leastInterval(["A","A","B","B","C","C","D","D","E"], 3))


    z = 0
    for case in testCases:
        resp = s.leastInterval(case[0], case[1])

        if resp == case[2]:
            print("[passed case {}]".format(z))

        elif resp != case[2]:
            print("[failed case {}] wanted {} got {}".format(z, case[2], resp))


        z += 1

# Case three, retired :)
            # print(d)
            #
            # ans = 0
            # ansS = ""
            #
            # while True:
            #     t = n
            #     lead = sortedD[0]
            #     i = 0
            #     l = len(sortedD)
            #
            #     if len(ansS) >= n+1:
            #         # Find the nearest lead
            #         # closest to the end
            #         # if lead is too close,
            #         # add spaces as required
            #         di = 0
            #         z = len(ansS)-1
            #
            #         while ansS[z] != lead:
            #
            #             if z < 0:
            #                 print("houston, we have a problem")
            #                 break
            #
            #             di += 1
            #             z -= 1
            #
            #         if len(" "*(n-di)) == 1 and ansS[0] not in ansS[len(ansS)-n-1:]:
            #
            #             tmp = ansS[0]
            #             ansS = ansS[1:] + tmp
            #         else:
            #             ansS += " "*(n-di)
            #
            #     while i < l:
            #
            #         if t == 0:
            #             t = n
            #             i = 0
            #
            #         ans += 1
            #
            #         ansS += sortedD[i]
            #
            #         d[sortedD[i]] -= 1
            #
            #         if sortedD[i] != lead:
            #             t -= 1
            #
            #         if d[sortedD[i]] == 0:
            #             if sortedD[i] == lead:
            #                 try:
            #                     lead = sortedD[i+1]
            #
            #                 except:
            #                     print(d)
            #                     print(ansS)
            #                     return len(ansS)
            #                     # return ans
            #
            #             del sortedD[i]
            #             i -=1
            #             l = len(sortedD)
            #
            #         i += 1
            #
            # return ans
