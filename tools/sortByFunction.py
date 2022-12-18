
'''
sort based upon the output of a function
'''
# https://docs.python.org/3/library/functools.html
#functools.cmp_to_key(func)

from functools import cmp_to_key

class Solution():
    def largestNumber(self, nums):
        compare = lambda a, b: -1 if a+b > b+a else 0

        sortedList = sorted(map(str, nums), key=cmp_to_key(compare))

        return str(int("".join(sorted(map(str, nums), key=cmp_to_key(compare)))))

print(Solution().largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]))
