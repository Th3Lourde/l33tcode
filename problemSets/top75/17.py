class Solution:
    def letterCombinations(self, digits):
        numToChrs = {
            "1": [],
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z'],
        }

        n = len(digits)

        if n == 0:
            return ""

        combos = set()

        def itr(combo, idx):
            if idx >= n:
                combos.add(combo)
                return

            for opt in numToChrs[digits[idx]]:
                itr(combo+opt, idx+1)

        itr("", 0)

        ans = []

        for combo in combos:
            ans.append(combo)

        return ans

print(Solution().letterCombinations("2"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("23"))
