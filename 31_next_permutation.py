
'''
Ok so we want a way to be able to 'get'
the next lexicographic permutation of a list

If we are at the 'end' of the order, return
list in ascending order
'''




class Solution:
    def nextPermutation(self, nums):

        atEnd = True

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                atEnd = False


        if atEnd:
            # Sort in ascending order
            nums.sort()


        elif not atEnd:
            ... # Find the next lexicographic permutation







if __name__ == '__main__':
    s = Solution()

    numList = [3,2,1]
    s.nextPermutation(numList)
    print(numList)
