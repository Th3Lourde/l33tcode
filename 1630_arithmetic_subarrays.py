
class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []
        for i in range(len(l)):
            subArr = list(nums[l[i]:r[i]+1])
            subArr.sort(reverse=True)

            dist = subArr[0]-subArr[1]
            isArith = True

            for i in range(len(subArr)-1):
                if subArr[i]-subArr[i+1] != dist:
                    isArith = False
                    break

            ans.append(isArith)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
