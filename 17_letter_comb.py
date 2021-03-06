'''
Given a string containing digits 2-9,
return all possible letter combinations
that the number could represent.

recursive calls

(digits, idx, current_letters)

'''

class Solution:

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        num_chr = [
            [],              # 0
            [],              # 1
            ['a', 'b', 'c'], # 2
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]

        def itr(digits, idx, current_letters, ans):

            if len(current_letters) == len(digits):
                ans.append(current_letters)
                return


            for chr in num_chr[int(digits[idx])]:
                itr(digits, idx+1, current_letters+chr, ans)

        ans = []

        itr(list(digits), 0, "", ans)

        return ans



    # Works
    def letterCombinations_1(self, digits):
        d = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g", "h", "i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        ans = []

        for i in range(len(digits)):
            if i == 0:
                ans += d[digits[i]]

            elif i != 0:
                new = []

                for z in range(len(ans)):
                    base = ans[z]

                    for j in range(len(d[digits[i]])):
                        new.append(base+d[digits[i]][j])

                ans = new

        return ans


if __name__ == '__main__':
    s = Solution()

    st = "23"

    print(s.letterCombinations(st))

    t = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    print(t)
