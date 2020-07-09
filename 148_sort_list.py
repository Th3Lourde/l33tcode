

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} --> {}".format(self.val, self.next)


'''
Prompt: Given a linked list, sort it in O(n log(n)) with constant space

Ok so how would I sort a linked list? I'm guessing that I would use quick sort since
I'm pretty sure that it has O(n log(n)) time complexity, I know that it has constant space


Let's do brute force first
Nah

Let's try merge sort
The trick here is going to be splitting up the input,
We are going to be given a singly-linked list so we'll have to
be manufacturing points of sorts in order to keep track of where
the beginning of the linked list is.

There's two parts to this algorithm, the part where the array is split up, and the other
part where the array is put back together. One thing we are certainly going to need to
do is to get the length of the array

1 --> 2 --> 3 --> 4 --> 5 --> 6

1 --> 2 --> 3 | 4 --> 5 --> 6

You could save the memory addresses of the different nodes, however that would violate
the limitation that you are supposed to keep the memory complexity to O(c)

Have two nodes, one rests at a minimum value of sorts, the other node is exploring.
You would update what comes after node one based upon where node two is.

Let's brute force this first.

If we were doing 0(n log n) this would imply a quicksort algo.

People say that we can do with with merge sort but idk

singly linked list, so can't really use quicksort, unless we make
the ll an array.

convert to arr, solve via qs or mergesort, convert back to ll.

Let's write this solution first.

How would we do this with mergesort?

If we can only return the nodes that we
initially started with, then use a dict to map
new node to old node.

'''



class Solution:

    def sortList(self, head):

        if not head: return None

        arr = []

        node = head

        while node:
            arr.append(node.val)
            node = node.next

        def qs(arr):
            def swap(arr, i, j):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

            def partition(arr, lo, hi):
                piv = arr[lo]
                i = lo
                j = hi

                while True:
                    while arr[i] < piv: i += 1
                    while arr[j] > piv: j -= 1

                    if i >= j: return j

                    swap(arr, i, j)
                    i += 1
                    j -= 1

            def sort(arr, lo, hi):
                if lo < hi:
                    piv = partition(arr, lo, hi)
                    sort(arr, lo, piv)
                    sort(arr, piv+1, hi)

            sort(arr, 0, len(arr)-1)

        qs(arr)

        head = ListNode(arr[0])
        node = head

        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next

        return head




    def sortList_1(self, head): # old attempt, never finished
        p1 = head
        p2 = head.next

        if p2 == None:
            return p1

        switch = False

        '''

        p1 --> p2 --->

        tmp = p2

        p1.next = p2

        p1 --> p1 --->


        '''

        while switch == False:

            switch = False

            while p2 != None:
                if p1.val > p2.val:
                    tmp = p2
                    p1.next = ListNode(p1.val)
                    p1.next.next = tmp.next
                    tmp.next = p1



# The linked list nodes must be
# adjacent to each other.

# They don't have to be, but the
# algo will fail if this is not
# true

# n1 is before n2

def switch_ll_n(n1,n2):
    tmp = n2

    n1.next = ListNode(n1.val)
    n1.next.next = tmp.next

    n1 = n2

    print(n1)

    return n1





if __name__ == '__main__':

    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)

    head.next = a
    a.next = b

    print(head)

    head = switch_ll_n(head,a)

    print(head)
