'''
mxn grid

accounts[i][j] == money i^th customer has in j^th bank


return the max wealth that a customer has in the bank


'''

class Solution:
    def maximumWealth(self, accounts):
        ans = 0

        for customer in accounts:
            tmp = 0
            for account in customer:
                tmp += account
            ans = max(tmp, ans)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.maximumWealth([[1,2,3],[3,2,1]]))
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))
    print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
