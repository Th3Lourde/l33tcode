

class Solution:
    def letterCombinations(self, digits):
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
