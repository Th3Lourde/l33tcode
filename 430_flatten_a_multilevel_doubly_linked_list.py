'''
Given doubly linked list

has .prev .next .child

.prev, .next moves l<-->r on x plane
.child moves on the y plan (only down)

flatten the list ∋ all the nodes appear in a single-level,
doubly linked list.

We are given the head.

Gist, we want to point all down to right
and then connect things after.

.next = []

while node or next
if not node.child:
    keep going

if node.child:
    next.append(node.next)

1 --> 2 --> 3 --> 4 --> 5 --> 6
            ^
            7 --> 8 --> 9 --> 10
                  ^
                  11 --> 12

1, 2, 3

next = [4]
set child as tmp
point node to child, next,
set node = tmp

1 --> 2 --> 3 --> 7 --> 8 --> 9 --> 10
                        ^
                       11 --> 12
  4 --> 5 --> 6

7, 8

next = [4,9]
set child as tmp
point node to child, next, prev
set node = tmp

1 --> 2 --> 3 --> 7 --> 8 --> 11 --> 12

11, 12

if not node.next and next:   <--- have this as a check before node = node.next
    tmp = next.pop()              avoid node = None
    node.next = tmp
    tmp.prev = node
    node = tmp

node = 9

1 --> 2 --> 3 --> 7 --> 8 --> 11 --> 12 --> 9 --> 10

  4 --> 5 --> 6

next = [4]

9, 10

if not node.next ...

1 --> 2 --> 3 --> 7 --> 8 --> 11 --> 12 --> 9 --> 10 --> 4 --> 5 --> 6

if not node.next and not next:
    return head


1 --> 2 --> 3 --> 4 --> 5 --> 6
            ^
            7 --> 8 --> 9 --> 10
                  ^
                  11 --> 12

next = []
node = 1

next = []
node = 2

next = []
node = 3

tmp = 7
next.append(3.next = 4)  | next = [4]

3.next = 7
7.prev = 3
3.child = None

node = 7

next = [4]
node = 7

next = [4]
node = 8

tmp = 11
next = [4,9]
8.next = 11
11.prev = 8
8.child = None

node = 11


node = 11
next = [4,9]


node = 12
next = [4,9]


tmp = 9
12.next = 9
9.prev = 12
node = 9

node = 9
next = [4]


node = 10
next = [4]

tmp = 4
10.next = 4
4.prev = 10
node = 4

node = 4
next = []

node = 5
next = []

node = 6
next = []

I failed to take into consideration if the child occurs at the end.

child at lhs
child at rhs

'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head): # made small mistake for RHS, else good.

        if not head: return None

        next = []
        node = head

        while node or next:
              # found child
            if node.child:
                tmp = node.child

                if node.next:
                    next.append(node.next)

                node.next = tmp
                node.next.prev = node
                node.child = None

                node = tmp

                # normal case
            elif node.next:
                node = node.next

                # end of line but []
            elif not node.next and next:
                tmp = next.pop()
                node.next = tmp
                tmp.prev = node

                node = tmp

                # end of line and not []
            elif not node.next and next == []:
                return head
