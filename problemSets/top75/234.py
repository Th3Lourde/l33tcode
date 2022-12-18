'''
Given the head of a singly linked list,
return true is the ll is a palindrome.
ll --> arr, check if pali
'''


class Solution:
    def isPalindrome(self, head):
        arr = []

        node = head

        while node:
            arr.append(node.val)
            node = node.next

        l = 0
        r = len(arr)-1

        while l < r:
            if arr[l] != arr[r]:
                return False

            l += 1
            r -= 1

        return True
