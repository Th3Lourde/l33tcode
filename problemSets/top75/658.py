from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        idx = bisect_left(arr, x)

        if idx == n or idx > 0 and abs(arr[idx-1]-x) <= abs(arr[idx]-x):
            idx -= 1

        print(idx)

        start, end = idx, idx

        for _ in range(k-1):
            if start == 0:
                end += 1
            elif end == n-1:
                start -= 1
            else:
                dist1 = abs(arr[start-1]-x)
                dist2 = abs(arr[end+1]-x)

                if dist1 <= dist2:
                    start -= 1
                else:
                    end += 1

        return arr[start:end+1]

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        ind = bisect_left(arr, x)
        if ind == n or ind > 0 and arr[ind] + arr[ind-1] >= 2*x:
            ind -= 1

        print(ind)

        beg, end = ind, ind
        for i in range(k-1):
            if beg == 0: end += 1
            elif end == n-1: beg -= 1
            else:
                if arr[end+1] + arr[beg-1] >= 2*x:
                    beg -= 1
                else:
                    end += 1

        return arr[beg:end+1]

print(Solution().findClosestElements([1], 1, 1))
print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
print(Solution().findClosestElements([1,2,3,4,5], 4, -1))


arr = [1,3,5,7]
bisect_left(arr, 2 )
