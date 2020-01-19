
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:


    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        headv = head

        while True:
            if type(headv.val) == str:
                return True
            elif type(headv.val) == int:
                headv.val = str(headv.val)
                if headv.next == None:
                    return False
                elif headv.next != None:
                    headv = headv.next


    def hasCycle1(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            # return True
            return False

        d = {}
        headv = head

        while True:
            try:
                d[headv.val] += 1
                # return False
                return True
            except:
                d[headv.val] = 1

            if headv.next == None:
                # return True
                return False
            elif headv.next != None:
                headv = headv.next


def fuzz():
    b = {}
    a = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]

    for i in range(len(a)):
        try:
            b[a[i]] += 1
        except:
            b[a[i]] = 1

    print(b)


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    s = Solution()

    # fuzz()

    r = s.hasCycle(a)
    print(r)
