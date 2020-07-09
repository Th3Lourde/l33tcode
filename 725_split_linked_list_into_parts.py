'''
Given a singly linked list with head node
root, write a function that splits the list
into k consecutive linked list 'parts'.

Step one, get the length of the linked list.

How might we be able to do this in one pass?
Not sure. Let's do the two pass solution first
and then come back if we need to.

1) get the length of the linked list.
Use this information to calculate how long each
sublist should be.

[1,2,3], k = 5
n = 3

ans = [0,0,0,0,0]

loop through n, adding one
to each element of ans.

mod it so it goes back to the
beginning of the list.

ans = [1,1,1,0,0]

node = head

for e in ans:
    start = node

    for i in range(1, e):
        node = node.next

    end = node
    node = node.next
    end.next = None

    ansNode.append(start)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3

ans = [0,0,0]
# n = 10, k = 3 <-- Yea I still haven't figured this out. Or have I? IDK
ans = [4,3,3]

node = 1

start = 1

for i in range(1,4):  <-- Happens three times, node = 4
    node = node.next

end = 4
node = 5
end.next = None
ansNode.append(start: 1-4)

node = 5
start=5
for i in range(1,3):
    node = node.next
node = 7
end 7
node = 8
...

I'm sure we could figure out some mod trick.
Do after we solve brute-force.

Time complexity:
0(2n) ⟹ 0(n)

Space complexity:
0(k) + 0(n)
^       ^
ans     ansNode

So we can actually have null elements in our answer.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

def createLL(arr):
    nodes = []

    for e in arr:
        nodes.append(ListNode(e))

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    return nodes[0]

class Solution:
    def splitListToParts(self, root, k): # This works, good run-time/memory

        if not root: return [None]*k

        if k == 1: return [root]

        # 1) Get the length of the ll
        n = 0

        node = root
        z = 0
        ans = [0 for i in range(k)]

        while node:
            node = node.next
            ans[z] += 1
            z += 1

            if z >= len(ans):
                z = 0

        node = root
        ansNode = [None]*k

        for z in range(len(ans)):
        # for e in ans:
            e = ans[z]
            start = node

            if not node: return ansNode

            for i in range(1, e):
                node = node.next

                if not node:
                    ansNode[z] = start
                    return ansNode

            end = node

            node = node.next

            end.next = None

            ansNode[z] = start

        return ansNode


if __name__ == '__main__':
    s = Solution()

    print(s.splitListToParts(createLL([1,2,3]), 3))
    print(s.splitListToParts(createLL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 6))
