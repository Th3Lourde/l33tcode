'''
Ok so I totally didn't read directions ♡

We care about returning a list of integers

We wish to return an array that has the k-values
for the different pancake flips that we have done.



'''

class Solution:
    def pancakeSort(self, arr):
        flips = []

        def flip(arr, k):
            l = 0
            r = l + k - 1

            while l < r:
                tmp = arr[l]
                arr[l] = arr[r]
                arr[r] = tmp

                l += 1
                r -= 1

            flips.append(k)

        for i in range(len(arr)-1, -1, -1):
            maxV = i

            for j in range(i-1, -1, -1):
                if arr[j] > arr[maxV]:
                    maxV = j

            if maxV != i:
                # Want to get the max element
                # to the front
                flip(arr, maxV+1)

                # Now we want to put it at i,
                # So we are flipping the first i+1 elements
                flip(arr, i+1)

        return flips

if __name__ == '__main__':
    s = Solution()

    print(s.pancakeSort([5,2,1,3,4]))
