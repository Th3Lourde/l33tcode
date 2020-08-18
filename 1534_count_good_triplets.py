'''
Given an array of integers, arr

and three integers, a,b,c

Find the number of good triplets
that exist.

A triplet (arr[i], arr[j], arr[k]) is
good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c

So this problem is pretty basic. There's the
matter of looping through all possible combinations
of i,j,k.

Then there's the matter of evaluating whether or
not a triplet is "good".

So I'm thinking one function to iterate through the
different triplets, and another function to classify
a given triplet as 'good' or 'bad'.

Let's see if I remember that itr algo:

[3,0,1,1,9,7]
   i j     k



def tripleIsGood(t):
    if t[0] < t[1] < t[2] and




'''

class Solution:

    def countGoodTriplets(self, arr, a, b, c):
        i = 0
        ans = 0

        def tripleIsGood(i, j, k):
            if 0 <= i < j < k and abs(arr[i]- arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                return True

        for i in range(0, len(arr)-2):
            k = len(arr)-1

            while i + 1 != k:
            # for k in range(k, i+2, -1):
                if i+1 != k:

                    for j in range(i+1, k):

                        if tripleIsGood(i, j, k):
                            # print("({}, {}, {})".format(arr[i], arr[j], arr[k]))
                            ans += 1

                k -= 1

        return ans

if __name__ == '__main__':
    s = Solution()

    s.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)

    s.countGoodTriplets([1,1,2,2,3], 0, 0, 1)
