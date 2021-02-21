'''
Got it right with some pretty tight code, yay me!
However, there are some even quicker ways of doing
it :)
'''

class Solution:

    def findNextSmallest(self, arr1, idx1, arr2, idx2):
        if idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] < arr2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        elif idx1 < len(arr1):
            idx1 += 1

        else:
            idx2 += 1

        return idx1, idx2

    def findMin(self, arr1, idx1, arr2, idx2):
        if idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] < arr2[idx2]:
                return arr1[idx1]
            else:
                return arr2[idx2]

        elif idx1 < len(arr1):
            return arr1[idx1]

        else:
            return arr2[idx2]

    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        isOdd = length%2 # ifIsodd == 1, yes, else no.
        p1, p2 = 0, 0

        itr = length//2
        if isOdd == 0:
            itr -= 1

        for i in range(itr):
            p1, p2 = self.findNextSmallest(nums1, p1, nums2, p2)

        if isOdd == 1:
            return self.findMin(nums1, p1, nums2, p2)

        ans1 = self.findMin(nums1, p1, nums2, p2)

        p1, p2 = self.findNextSmallest(nums1, p1, nums2, p2)

        ans2 = self.findMin(nums1, p1, nums2, p2)

        return (ans1+ans2)/2


if __name__ == '__main__':
    s = Solution()

    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))
    print(s.findMedianSortedArrays([0,0], [0,0]))
    print(s.findMedianSortedArrays([], [1]))
    print(s.findMedianSortedArrays([2], []))
