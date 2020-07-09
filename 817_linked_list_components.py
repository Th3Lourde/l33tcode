'''
Given the head of a linked list
the ll only has unique vals
Given g int[], contains some of the values of the ll

Return the number of components of g that are connected.

g = [a,b]
ll = a --> b

a maps to b, which is one connected 'group'. So the ans is 1.

g = [a,b,d,e,g,h,i]
ll = a --> b --> c --> d --> e --> f --> g --> h --> i
     (     )           (     )           (           )

ans = 3

g = [a]
ll = a --> b

ans = 0 ?

How to code this:
1) Create dict that answers the question of "is this node.val in g?"
type(a) == 'int'
dict = {a:True, b: True, ...}

ans = 0
run = 0

step through all nodes in head.
for each node, check if node ∈ G.

if ∈ G and run == 0:
    run = 1

elif ∈ G and run > 0:
    run += 1

elif ∉ G and run > 1:
    # have reached end of run
    ans += 1
    run = 0

If we seen an element that is connected, at 1 to run.
If we see an element that is not connected, check to see
if our run > 1. If it is, then we have seen at least two
elements that are connected.

After our loop, check on status of run.

if run > 1: return ans +=1

return ans

I should practice differentiating between a dictionary
and a set. Use a set if we want to know whether or not
something exists.

Use a dict if we care about the associated value.

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

class Solution:

        # Set implementation
    def numComponents(self, head, G):

        if G == []: return 0

        s = set()

        for g in G:
            s.add(g)

        ans = 0
        run = 0
        node = head

        while node:
            if node.val in s and run == 0:
                run = 1

            elif node.val in s and run > 0:
                run += 1

            elif node.val not in s and run < 1:
                run = 0

            elif node.val not in s and run >= 1:
                # have reached end of run
                ans += 1
                run = 0

            node = node.next

        if run >= 1: return ans + 1

        return ans


    def numComponents_dict(self, head, G): # Works, used dict, not set.

        # G ⊂ Head, so if Head == [] ⟹ G == []
        if G == []: return 0

        d = {}

        for g in G:
            d[g] = True

        ans = 0
        run = 0
        node = head

        while node:
            if node.val in d and run == 0:
                run = 1

            elif node.val in d and run > 0:
                run += 1

            elif node.val not in d and run < 1:
                run = 0

            elif node.val not in d and run >= 1:
                # have reached end of run
                ans += 1
                run = 0


            node = node.next

        if run >= 1: return ans + 1

        return ans


if __name__ == '__main__':
    s = Solution()

    zero = ListNode(0)
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)
    seven = ListNode(7)

    zero.next = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven

    print(s.numComponents(zero, [0,3,1]))
