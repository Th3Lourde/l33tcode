'''
"PP", "LP", "PL", "LL"
"AP", "PA", "AL", "LA",

n | output
0 | 0
1 | 3
2 | 8

'''

class Solution:
    def checkRecord(self, n):
        dp = [set(), set({"P","L","A"})]

        # Ok so we want to add a character onto every
        # Already existing sequence
        # From one sequence, we can spawn up to three
        # more sequences

        for idx in range(2, n+1):
            nextRecords = set()

            for record in dp[idx-1]:
                if "A" not in record:
                    nextRecords.add(record+"A")

                if not(len(record) >= 2 and record[-2:] == "LL"):
                    nextRecords.add(record+"L")

                nextRecords.add(record+"P")

            dp.append(nextRecords)

        # print(dp)

        return len(dp[n])


print(Solution().checkRecord(1))
print(Solution().checkRecord(2))
print(Solution().checkRecord(100))
