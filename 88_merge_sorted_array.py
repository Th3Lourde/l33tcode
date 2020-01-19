

class Solution:

    def merge(self, nums1, m: int, nums2, n: int) -> None:
        p1 = m-1
        p2 = n-1
        p3 = n+m-1

        '''
        Edge Cases
        nums1 == []
        nums2 != []

        nums1 != []
        nums2 == []

        Hit bottom code if both nums1 != [] and nums2 != []
        '''
        if nums1 == [] and nums2 != []:
            nums1 = nums2
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        # elif nums1 != [] and nums2 == []:
        #     # Can delete
        #     # Won't enter while-loop b/c
        #     # p2 == 0
        #     nums1 = nums1


        # while p1 >= 0 and p2 >= 0 and p3 >= 0:
        while True:

            # If we have run out of terms
            # in nums1
            if p1 < 0 and p2 >= 0:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1

            # If we have run out of terms
            # in nums2
            elif p2 < 0 and p1 >= 0:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1

            elif p1 < 0 and p2 < 0:
                break

            ## If none of the pointers
            ## are less than zero
                
            # if val in nums1 is greater
            elif nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1

            # if val in nums2 is greater
            elif nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1


    def merge2(self, n1, m, n2, n) -> None:
        to_kill = n

        if len(nums2) == 0:
            return nums1
        elif len(nums1) == 0 and len(nums2) != 0:
            nums1 = nums2

        stop = m

        j = 0
        i = 0

        while True:
            # When we hit the zeros
            if i == stop:
                for z in range(j,n):
                    nums1[i] = nums2[z]
                    # nums1.insert(i, nums2[z])
                    i += 1

                break

            elif nums1[i] <= nums2[j]:
                i += 1
            # When n2 term is less than
            # n1 term
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                to_kill -= 1
                j += 1
                i += 1
                stop += 1
                if j == n:
                    break

        # Kill teh zeros
        for i in range(n-to_kill):
            nums1.pop()



    def merge1(self, n1, m, n2, n):
        # Merge the two lists

        stop = m

        j = 0
        i = 0

        while True:
            # When we hit the zeros
            if i == stop:
                # Fill in the rest
                # Current index is at a zero
                for z in range(j, n):
                    n1.insert(i, n2[z])
                    i += 1
                break
            # When current n1 term is less
            # than current n2 term
            elif n1[i] <= n2[j]:
                i += 1
            # When n2 term is less than
            # n1 term
            elif n1[i] > n2[j]:
                n1.insert(i, n2[j])
                j += 1
                i += 1
                stop += 1
                if j == n:
                    break

        n1 = n1[:(m+n)]

        return n1


if __name__ == '__main__':
    s1 = Solution()

    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1

    print("num1: {} num2: {}".format(nums1, nums2))

    r = s1.merge(nums1, m, nums2, n)


    print(r)
