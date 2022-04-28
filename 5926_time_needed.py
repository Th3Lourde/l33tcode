'''
[2,3,2]
[1,2,1]

while tickets

'''

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):
                if i == k and tickets[i] == 1:
                    return time + 1

                elif tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1

print(Solution().timeRequiredToBuy([2,3,2], 2))
print(Solution().timeRequiredToBuy([5,1,1,1],  0))
