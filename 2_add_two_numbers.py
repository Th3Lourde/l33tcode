
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{} --> {}".format(self.val, str(self.next))


'''
[9,9,9,9,9,9,9]
       1

[9,9,9,9]
       2

[8,9,9, ]
       3

tmp = 1





'''

class Solution:

    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2

        v = p1.val + p2.val

        ans = ListNode(v%10)
        tmp = int((v - v%10)/10)

        p1 = p1.next
        p2 = p2.next
        p3 = ans

        while p1 and p2:
            v = p1.val + p2.val + tmp

            p3.next = ListNode(v%10)

            tmp = int((v - v%10)/10)

            p1 = p1.next
            p2 = p2.next
            p3 = p3.next

        # Check if p1 or p2
        if p1 or p2:
            if p1:
                p3.next = p1

            else:
                p3.next = p2


            p = p3.next

            while p:
                s = p.val + tmp
                p.val = s%10
                tmp = max(0, int((s - s%10)/10))

                if tmp == 0:
                    break

                p3 = p3.next
                p = p.next

        if tmp:
            p3.next = ListNode(tmp)

        return ans
        # Works, 10/15/19
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        tens = 0

        n1 = l1
        n2 = l2

        ans = ListNode(0)
        a = ans

        while True:
            tmp = n1.val + n2.val + tens

            if tmp >= 10:
                ans.val = tmp-10
                tens = tmp//10

            elif tmp < 10:
                ans.val = tmp
                tens = 0

            if (n1.next != None) and (n2.next != None):
                n1 = n1.next
                n2 = n2.next
            elif (n1.next != None) and (n2.next == None):
                # Finished n2, follow n1
                n2.val = 0
                n1 = n1.next
            elif (n1.next == None and n2.next != None):
                # Finished n1, follow n2
                n1.val = 0
                n2 = n2.next
            elif (n1.next == None and n2.next == None):
                # Done with both lists
                # ans.next = None

                if tens == 0:
                    return a
                elif tens != 0:
                    ans.next = ListNode(tens)
                    return a


            ans.next = ListNode(0)
            ans = ans.next



def generateLL(arr):
    nodes = []

    for e in arr:
        nodes.append(ListNode(e))

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    return nodes[0]


if __name__ == '__main__':
    a = generateLL([9,9,9,9,9,9,9])
    b = generateLL([9,9,9,9])

    print(a)
    print(b)

    s = Solution()

    print(s.addTwoNumbers(a, b))
