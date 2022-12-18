class Solution:
    def accountsMerge(self, accounts):
        newAccounts = []

        for account in accounts:
            newAccounts.append([account[0], set(account[1:])])

        updated = True

        # print("-------------------")

        while updated:
            # Go through each account and perform a merge
            i = 0
            updated = False

            # print(newAccounts)

            while i < len(newAccounts):
                name, emailSet = newAccounts[i]
                skipList = []
                tmpAccounts = []

                for idx in range(len(newAccounts)):
                    if i == idx:
                        continue

                    _, compareSet = newAccounts[idx]

                    if emailSet.intersection(compareSet) != set():
                        # Have intersection
                        updated = True
                        emailSet = emailSet.union(compareSet)


                        skipList.append(idx)

                # Update the emailSet
                # print(skipList)
                newAccounts[i][1] = emailSet

                for idx, val in enumerate(newAccounts):
                    if idx not in skipList:
                        tmpAccounts.append(val)

                newAccounts = tmpAccounts
                i += 1

            # print("-------------------")

        # print(newAccounts)
        # return newAccounts

        resp = []

        for idx in range(len(newAccounts)):
            term = [newAccounts[idx][0]]

            rhs = list(newAccounts[idx][1])
            rhs.sort()

            term = term + rhs

            resp.append(term)

        return resp

print(Solution().accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]))
