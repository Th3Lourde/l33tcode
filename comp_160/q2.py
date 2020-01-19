

class Solution:

    def maxLength(self, arr):
        print(arr)

        d = {}

        for i in range(len(arr)):
            d[i] = {}

            for j in range(len(arr[i])):
                d[i][arr[i][j]] = True



        for i in range(1, len(arr)):
            # i represents the size of the sub-string
            for k in range(len(arr)-i)






        # 1) Create set for each subarray




        return ":)"
'''
Given an array of strings, find the
length of the largest combination of
the array s.t. that combination is
composed of unique characters

Make a dictionary, where the keys are the indicies of the subarray and the values are another dictionary.
We are basically creating a basterdized set.

Do we want to start from the bottom or the top?
Let's try starting from the bottom.


'''


if __name__ == '__main__':
    s = Solution()

    arr = ["un","iq","ue"]

    print(s.maxLength(arr))
