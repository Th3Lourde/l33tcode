'''
Ok so this will always work.
Maybe we should have a different call
for when we apply the algorithm to the
left or right array. We'll see.

If diff > 6:
    pick largest value from n1
    pick smallest value from n2
    use whichever one is closer

if diff > 5:
    pick largest value < 6 from n1
    pick largest value < 6 from n2
    use whichever one is closer

...

'''
class Solution:
    def minOperations(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        if abs(n-m)>=6:return -1

        s1 = sum(nums1)
        s2 = sum(nums2)
        n1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        n2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

        for n in nums1:
            n1[n] += 1

        n1Key = list(n1.keys())
        n1Key.sort()

        for n in nums2:
            n2[n] += 1

        n2Key = list(n2.keys())
        n2Key.sort()

        def getKey(lMax, rMax, left, right):
            rl = -1
            rr = -1
            for l in left:
                if l < lMax:
                    rl = max(rl, l)

            for r in right:
                if r < rMax:
                    rr = max(rr, r)

            return rl, rr


        while s1 != s2:
            diff = abs(s1-s2)

            lTarg = 0
            rTarg = 0

            if diff >= 5:
                lTarg = 6
                rTarg = 1
                #6,1
            elif diff >= 4:
                lTarg = 5
                rTarg = 2
                #5,2
            elif diff >= 3:
                #4,3
            elif diff >= 2:
                # 3,4
            elif diff >= 1:
                #2,5















if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([1,1,1,1,1,1,1], [6]))
