'''
Find all possible combinations of k
numbers that add up to a given number n

Only numbers from [1,9] can be used.

Each combination should be unique.

K → the number of numbers we can use to sum
N → the end result of the sum

Ok so similar problem, use recursive calls to
solve the problem.

sum = [0 for i in range(k)]

-------------------------------------------------------
# terms → list of ints we are using for our sum
# sum → current sum
# opts → list of ints we can add to our sum

# Also, only make a recursive call if the sum < n

(terms, i, sum, opts)

if i == len(terms)
    if sum == n:
        # Check that our combination is unique
        # If unique, add it to ans

    return


for j in range(len(opts)):
    opt = opts[j]

    if sum + opt <= n:
        terms[i] = opt
        recurse(term, i+1, sum+terms[i], opts[:j] + opts[j+1:] )






'''

class Solution:
            # This works, however isn't very fast.
            # I wonder what a quicker solution might
            # be.
    def combinationSum3(self, k, n):
        ans = []
        seen = set()

        def itr(terms, i, sum, opts):
            if i == len(terms):
                if sum == n:
                    termsT = list(terms)
                    termsT.sort()
                    termsT = tuple(termsT)

                    if termsT not in seen:
                        seen.add(termsT)
                        ans.append(list(terms))
                return

            for j in range(len(opts)):
                if sum + opts[j] <= n:
                    terms[i] = opts[j]

                    itr(terms, i+1, sum+terms[i], opts[:j]+opts[j+1:])

                    terms[i] = 0

        itr([0 for i in range(k)], 0, 0, [i for i in range(1,10)])

        return ans


if __name__ == '__main__':
    s = Solution()

    # print(s.combinationSum3(3, 7))

    print(s.combinationSum3(3, 9))
