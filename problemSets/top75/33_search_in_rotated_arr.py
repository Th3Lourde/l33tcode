class Solution:
    def search(self, arr, target):
        l = 0
        r = len(arr)-1

        if arr[l] == target:
            return l

        if arr[r] == target:
            return r

        while l < r:
            m = l + (r-l)//2

            if arr[m] == target:
                return m

            if arr[l] < arr[m]:
                if arr[l] <= target <= arr[m]:
                    r = m
                else:
                    l = m+1
                    if arr[l] == target:
                        return l
            else:
                if arr[m] <= target <= arr[r]:
                    l = m+1
                    if arr[l] == target:
                        return l
                else:
                    r = m

        return -1

print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))

print(Solution().search([4,5,6,7,0,1,2], 2))
