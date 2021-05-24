class Solution:
    def circularArrayLoop(self, nums):
        def getIndex(i):
            # print(i)
            tmpI = i + nums[i]
            if nums[i] > 0:
                return tmpI % len(nums)


            if tmpI < 0:
                if tmpI == -1:
                    return len(nums)-1
                else:
                    tmpI = tmpI % (-1*len(nums))
                    # print("tmpI: {}".format(tmpI))
                    return len(nums)+tmpI

            return tmpI


        def isCycle(i):
            initial = i
            s2 = set()
            pos = True

            if nums[i] < 0:
                pos = False

            while i not in s2:
                if (nums[i] > 0) != pos:
                    return False

                s2.add(i)
                i = getIndex(i)
                # print("Got: {}".format(i))

                if len(s2) > len(nums):
                    return False

            if initial != i:
                return False

            return len(s2) != 1

        for i in range(len(nums)):
            if isCycle(i):
                return True

        return False

s = Solution()



print(s.circularArrayLoop([-2,-3,-9])) # False

print(s.circularArrayLoop([-1,-2,-3,-4,-5])) # False
print(s.circularArrayLoop([3,1,2])) # True
print(s.circularArrayLoop([-1,2])) # False
print(s.circularArrayLoop([-2,1,-1,-2,-2])) # False
print(s.circularArrayLoop([2,-1,1,2,2])) # True
