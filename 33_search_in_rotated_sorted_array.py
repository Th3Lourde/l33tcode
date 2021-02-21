'''
Log:
    3/25/20
    Wrote the initial run-through of the problem. I believe I have the right answer,
    however my solution is not fast enough.

    3/26/20
    Looked at the algorithm, saw that when I was creating a sublist that I was checking
    both lists. I only need to check one (b/c reasons). I wrote out the logic of why I
    only need to check one, and then I did it.

    Still not fast enough. I think that this is due to my recursion calls. Hope to make
    progress on that tomorrow

    3/27/20
    Today I am going to re-write the code so there is no recursion.

    1/9/20
    I am going to write a solution that solves in log(n) time, deleted the old
    code work

    brute force solution: single pass through list 0(n)
    my solution: modified binary search


'''

class Solution:
    def search(self, nums, target):
        ans = -1

        l = 0
        r = len(nums)-1

        if nums[0] == target: return 0
        if nums[-1] == target: return len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] == target: return m

            if nums[l] < nums[m]:
                # left side is sorted
                if nums[l] <= target <= nums[m]:
                    # look left
                    r = m
                else:
                    # look right
                    l = m+1
            else:
                # right side is sorted
                if nums[m] <= target <= nums[r]:
                    # look right
                    l = m+1
                else:
                    # look left
                    r = m

        return ans

if __name__ == '__main__':
    s = Solution()

    testCases = [
        [[4,5,6,7,0,1,2], 0, 4],
        [[4,5,6,7,0,1,2], 3, -1],
        [[4,5,6,7,0,1,2], 8, -1],
        [[4,5,6,7,0,1,2], 5, 1],
    ]

    i = 0
    for test in testCases:
        ans = s.search(test[0], test[1])
        if ans != test[2]:
            print("[Error] for list: {} target: {} got {} wanted: {}".format(test[0], test[1], ans, test[2]))

        else:
            print("[passed] test case {}".format(i))

        i += 1
