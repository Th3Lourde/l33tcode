class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

class Solution:
    def insert(self, head, insertVal):
        if not head:
            head_node = Node(insertVal)
            head_node.next = head_node
            return head_node

        current = head

        while True:
            if current.val > current.next.val and (current.val <= insertVal or insertVal <= current.next.val):
                break

            elif current.val <= insertVal <= current.next.val:
                break

            elif current.next == head:
                break

            current = current.next

        new_node = Node(insertVal)

        new_node.next = current.next
        current.next = new_node

        return head

        print("Stopped at: {}".format(current.val))

def generateLL(vals):
    for idx in range(len(vals)):
        vals[idx] = Node(vals[idx])

    for idx in range(len(vals)-1):
        vals[idx].next = vals[idx+1]

    # vals[-1].next = vals[0]

    return vals[0]


ll = generateLL([1,2,3,4,5])

print(ll)


print(Solution().insert(None, 1))
print(Solution().insert(ll, 1))
