class Account:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = set(accounts)

    def to_output(self):
        account_list = list(self.accounts)
        account_list.sort()
        return [self.name] + account_list

    def __repr__(self):
        accounts = list(self.accounts)
        print(accounts)
        accounts.sort()
        print(accounts)

        return [self.name] + accounts

class Solution:
    def accountsMerge(self, accounts):
        account_list = []
        accounts_to_skip = set()
        n = len(accounts)

        for account in accounts:
            account_obj = Account(account[0], account[1:])
            account_list.append(account_obj)

        progress = True

        while progress:
            progress = False

            for idx in range(n):
                if idx not in accounts_to_skip:
                    for j in range(idx+1, n):
                        if j not in accounts_to_skip and len(account_list[idx].accounts.intersection(account_list[j].accounts)) > 0:
                            # print("Union of:")
                            # print("{}".format(account_list[idx].accounts))
                            # print("{}".format(account_list[j].accounts))
                            account_list[idx].accounts = account_list[idx].accounts.union(account_list[j].accounts)
                            progress = True
                            # print("{}".format(account_list[idx].accounts))
                            accounts_to_skip.add(j)

        ans = []

        for idx in range(n):
            if idx not in accounts_to_skip:
                ans.append(account_list[idx].to_output())

        return ans

print(Solution().accountsMerge( [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))

print(Solution().accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))



print(Solution().accountsMerge([["John","johnsmith@mail.com","johnzewyork@mail.com"],["John","johnsmith@mail.com","jahn00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
