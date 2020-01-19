

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

Bubble Sort:








'''



class Solution:
    def sortList(self, head):
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
