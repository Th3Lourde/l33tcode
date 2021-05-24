class Solution:
    def accountsMerge(self, accounts):
        accountNameToEmails = {}

        for account in accounts:
            if account[0] not in accountNameToEmails:
                accountNameToEmails[account[0]] = [set(account[1:])]
            else:
                accountNameToEmails[account[0]].append(set(account[1:]))

        mergedAccounts = []

        def uf(emails):
            mergesOccurred = False
            i = 0
            while i < len(emails):
                j = i+1

                while j < len(emails):
                    if emails[i].intersection(emails[j]) != set():
                        emails[i] = emails[i].union(emails[j])
                        del emails[j]
                        mergesOccurred = True
                    else:
                        j += 1
                i += 1
            return mergesOccurred

        for accountName in accountNameToEmails:
            emails = accountNameToEmails[accountName]

            accountsWereMerged = True

            while accountsWereMerged:
                accountsWereMerged = uf(emails)

            for emailSet in emails:
                emailList = list(emailSet)
                emailList.sort()
                account = [accountName] + emailList
                mergedAccounts.append(account)


        return mergedAccounts

print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

print(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
