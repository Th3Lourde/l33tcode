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


'''

class Solution:

    def search(self, nums, target): # This works

        if len(nums) == 0:
            return -1

        elif len(nums) == 1 and nums[0] != target:
            return -1

        elif len(nums) == 1 and nums[0] == target:
            return 0



        subList = nums
        s = 0
        e = len(nums)-1

        # Check that the target isn't equal to the endpoints

        while True:

            # Check that the outer bounds of the
            # interval do not equal the target

            if nums[s] == target:
                return s

            elif nums[e] == target:
                return e

            if (nums[s] < nums[e]) and (target >= nums[s] and target <= nums[e]):
                # Perform a search for the target
                # return target or -1
                while True:
                    if nums[s] == target:
                        return s

                    if nums[e] == target:
                        return e

                    if e-s == 1:
                        return -1

                    middle = int((e-s)/2) + s

                    if nums[middle] == target:
                        return middle

                    if nums[middle] > target:
                        e = middle

                    elif nums[middle] < target:
                        s = middle

            elif nums[s] > nums[e]:
                # Split the subList in half,
                # continue with the "correct" half
                middle = int((e-s)/2) + s
                # Check if middle == target

                if middle != s and middle != e:

                    if nums[s] < nums[middle] and not(nums[middle] < nums[e]):
                        # left sublist is sorted
                        if target <= nums[middle] and target >= nums[s]:
                            # target is in [nums[s], nums[middle]]
                            e = middle

                        else:
                            s = middle

                    elif not(nums[s] < nums[middle]) and nums[middle] < nums[e]:
                        # right sublist is sorted
                        if target <= nums[e] and target >= nums[middle]:
                            # target is in [nums[middle], nums[e]]
                            s = middle

                        else:
                            e = middle

                else:
                    return -1

            else:
                return -1




class Solution1:

    def recurse(self, nums, start, end, target):
        t = target
        # Check borders of interval
        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        '''
        If the target that we are searching for lies
        within the given interval... find it :)
        '''
        if (nums[start] < nums[end]) and (target > nums[start] and target < nums[end]):
            # Interval is ordered
            # perform binary search conditionally
            a = start
            b = end
            while True:

                if nums[a] == target:
                    return a

                if nums[b] == target:
                    return b

                if b-a == 1: # If there is no more room to guess
                    return -1

                middle = int((end-start)/2) + start

                if nums[middle] == target:
                    return middle

                if nums[middle] > target:
                    b = middle

                elif nums[middle] < target:
                    a = middle




        elif nums[start] > nums[end]:
            middle = int((end-start)/2) + start
            # Work out some logic about what to return and why...

            if middle != start and middle != end:

                # find which of the sublists are ordered
                if nums[start] < nums[middle] and nums[middle] < nums[end]:
                    # pivot is zero, check both
                    if t <= nums[middle] and t >= nums[start]:
                        return self.recurse(nums, start, middle, target)

                    elif t >= nums[middle] and t <= nums[end]:
                        return self.recurse(nums, middle, end, target)

                elif nums[start] < nums[middle] and not(nums[middle] < nums[end]):
                    # left sublist is sorted
                    if t <= nums[middle] and t >= nums[start]:
                        # target is in [nums[start], nums[middle]]
                        return self.recurse(nums, start, middle, target)

                    else:
                        return self.recurse(nums, middle, end, target)

                elif not(nums[start] < nums[middle]) and nums[middle] < nums[end]:
                    # right sublist is sorted
                    if t <= nums[end] and t >= nums[middle]:
                        # target is in [nums[middle], nums[end]]
                        return self.recurse(nums, middle, end, target)

                    else:
                        return self.recurse(nums, start, middle, target)

            else:
                return -1


    def search(self, nums, target):

        if len(nums) == 0:
            return -1

        a = nums[0]
        b = nums[-1]

        if a == target:
            return 0

        if b == target:
            return len(nums)-1

        if len(nums) > 2:
            tmp = self.recurse(nums, 0, len(nums)-1, target)

            if tmp:
                return tmp

            elif not tmp:
                return -1

        elif len(nums) <= 2:
            return -1







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
