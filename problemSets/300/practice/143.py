'''
1 --> 2 --> 3 --> 4 --> 5

-0-1-2-3-4-
[1,2,3,4,5]
     l
     r

head = 1 --> 5 --> 2 --> 4 --> 3
                         n
left = False
node = head


'''

class Solution:
    def reorderList(self, head):
        list = []
        node = head

        while node:
            list.append(node)
            node = node.next

        l = 0
        r = len(list)-1

        head = list[l]
        node = head
        l += 1
        left = False

        while l <= r:
            if left:
                node.next = list[l]
                l += 1

            else:
                node.next = list[r]
                r -= 1

            left = not left
            node = node.next

        node.next = None

        return head
