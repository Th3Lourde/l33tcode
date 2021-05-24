class Solution:
    def threeSum(self, arr):
        # arr.sort()
        dict = {}
        validSums = set()

        for idx, e in enumerate(arr):
            if e in dict:
                dict[e].add(idx)
            else:
                dict[e] = set({idx})

        for l in range(len(arr)-2):
            for r in range(l+1, len(arr)-1):
                targ = -1*(arr[l]+arr[r])

                if targ in dict:
                    validSum = [arr[l], arr[r], targ]
                    validSum.sort()

                    if tuple(validSum) not in validSums:
                        for z in dict[targ]:
                            if z != l and z != r:
                                validSum = [arr[z], arr[l], arr[r]]
                                validSum.sort()
                                validSums.add(tuple(validSum))
                                break

        # print(list(validSums))
        ans = []

        for validSum in validSums:
            ans.append(list(validSum))

        return ans

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        n = len(arr)

        for i in range(n-1):
            if i > 0 and arr[i-1] == arr[i]:
                continue

            targ = (-1)*arr[i]
            l, r = i+1, n-1

            while l < r:
                if arr[l]+arr[r] == targ:
                    ans.append([arr[l], arr[r], arr[i]])
                    l += 1
                    # Do something with l
                    while l < r and arr[l] == arr[l-1]: l += 1

                if arr[l]+arr[r] < targ:
                    l += 1
                else:
                    r -= 1
        return ans
