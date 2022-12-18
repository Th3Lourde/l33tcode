# https://leetcode.com/problems/linked-list-cycle-ii/
#https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions%3A-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained

'''
An explanation about finding the entry point part.
First assume when fast and slow meet, slow has moved a steps, and fast has moved 2a steps. They meet in the circle, so the difference a must be a multiple of the length of the circle.
Next assume the distance between beginning to the entry point is x, then we know that the slow has traveled in the circle for a-x steps.
How do we find the entry point? Just let slow move for another x steps, then slow will have moved a steps in the circle, which is a multiple of length of the circle.
So we start another pointer at the beginning and let slow move with it. Remember x is the distance between beginning to the entry point, after x steps, both pointer will meet at the entry of circle.

    https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
'''


class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        print("{}|{}".format(slow, fast))
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            print("{}|{}".format(slow, fast))
            if slow == fast: break

        print(slow)

        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
