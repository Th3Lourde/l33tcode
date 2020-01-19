class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + "-->" + str(self.next)

class Solution:

    # Do the thing with linear time and constant space
    def isPalindrome(self, head:ListNode) -> bool:
        # Ok so I can't actually use the sum, need to check
        # the order as well as the nums[i]s in the ll

        if head == None or head.val == None:
            return True

        # 1) Get length
        # Assuming that we are not given an empty LL
        headV = head
        l = 0

        while True:
            l += 1
            if headV.next != None:
                headV = headV.next
            elif headV.next == None:
                break

        if l <= 1:
            return True


        # Ok so now we have the length of the LL, how to proceed?
        # Iterate through LL again, putting nums[i]s into queue
        # after half-way point, check to make sure nums[i]s are equal

        if l%2 == 0:
            p = l/2
            same = int(p)
        elif l%2 != 0:
            p = (l+1)/2
            same = int((l-1)/2)

        headv = head
        tmp = None
        i = 1

        '''
        tmp = 3
        headv = 2
        i = 4

        B:
        1 --> 2 --> 3 --> 2 --> 1 --> None

        tmp2 = headv.next |  tmp2 = 1
        headv.next = tmp  |  2.next = 3
        tmp = headv       |  tmp = 2
        headv = tmp2      |  headv = tmp2 = 1

        tmp = 2
        headv = 1
        i = 5

        A:
        1 --> 2 --> 3 <-- 2 <-- 1 None
                                ^
        tmp2 = headv.next |  tmp2 = None
        headv.next = tmp  |  1.next = 2
        tmp = headv       |  tmp = 1
        headv = tmp2      |  headv = tmp2 = None

        We capture the next node to reverse
        We reverse the current node
        We store our current node
        We update our current node to the node in first line
        We conditionally update i
        '''


        while True:
            if i < p:
                headv = headv.next
                i += 1
            elif i == p:
                tmp = headv
                headv = headv.next
                i += 1

            elif i > p:

                tmp2 = headv.next
                headv.next = tmp
                tmp = headv
                if tmp2 != None:
                    headv = tmp2


                if i == l:
                    break
                elif i < l:
                    i += 1

        p1 = head
        p2 = headv

        for i in range(same):
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        return True



    # Ahh, can't use sum b/c order mattersssss
    def isPalindrome3(self, head:ListNode) -> bool:
        # Ok so I can't actually use the sum, need to check
        # the order as well as the nums[i]s in the ll

        if head == None or head.val == None:
            return True

        # 1) Get length
        # Assuming that we are not given an empty LL
        headV = head
        l = 0

        while True:
            l += 1
            if headV.next != None:
                headV = headV.next
            elif headV.next == None:
                break

        if l <= 1:
            return True


        # Ok so now we have the length of the LL, how to proceed?
        # Iterate through LL again, putting nums[i]s into queue
        # after half-way point, check to make sure nums[i]s are equal

        if l%2 == 0:
            flip = l/2
        elif l%2 != 0:
            flip = (l+1)/2

        i = 0
        queue = []
        while True:
            if i%2 == 0:
                if i <= flip:
                    queue.append(head.value)
                    i += 1
                    head = head.next
                elif i > flip:
                    r = queue.pop()
                    if r != head.val:
                        return False
                    elif r == head.val:
                        if i != l:
                            i += 1
                            head = head.next
                        elif i == l:
                            break
            elif i%2 == 1:
                if i < flip:
                    queue.append(head.value)
                    head = head.next
                    i += 1
                elif i == flip:
                    head = head.next
                    i += 1
                elif i > flip:
                    r = queue.pop()
                    if r != head.val:
                        return False
                    elif r == head.val:
                        if i != l:
                            i += 1
                            head = head.next
                        elif i == l:
                            break



        return True

        '''
        1 2 3 2 1

        queue = [1,2]
        halway = 3
        i = 4
        # Pop, check if same, return conditionally
        # if len(queue == 0) and i == length:
        #        return True
        '''



    def isPalindrome2(self, head:ListNode) -> bool:
        print(head)

        if head == None or head.val == None:
            return True

        # 1) Get length
        # Assuming that we are not given an empty LL
        headV = head
        l = 0

        while True:
            l += 1
            if headV.next != None:
                headV = headV.next
            elif headV.next == None:
                break

        if l <= 1:
            return True

        # From here we can either reverse the LL
        # or have some sort of counter that should
        # equal zero after we have finished iterating
        # through the loops

        skip = -1

        if l%2 != 0:
            skip = (l+1)/2
            print(skip)

        '''
        1 2 3 2 1
        '''

        i = 1
        ans = 0
        while True:
            if skip != -1:
                if i < skip:
                    ans += head.val
                    head = head.next
                    i += 1
                elif i == skip:
                    head = head.next
                    i += 1
                elif i > skip:
                    ans -= head.val
                    if i != l:
                        head = head.next
                        i += 1
                    elif i == l:
                        break
            elif skip == -1:
            # Use length
                if i <= int((l/2)):
                    ans += head.val
                    head = head.next
                    i += 1
                elif i > int((l/2)):
                    ans -= head.val
                    if i != l:
                        head = head.next
                        i += 1
                    elif i == l:
                        break

        return ans == 0

        '''
        1 2 3 2 1
        skip = 3
        i = 4
        ans = 0
        '''




    def isPalindrome1(self, head:ListNode) -> bool:

        print(head)

        if head == None or head.val == None:
            return True

        # 1) Get length
        # Assuming that we are not given an empty LL
        headV = head
        l = 0

        while True:
            l += 1
            if headV.next != None:
                headV = headV.next
            elif headV.next == None:
                break

        if l <= 1:
            return True

        # From here we can either reverse the LL
        # or have some sort of counter that should
        # equal zero after we have finished iterating
        # through the loops



        # 2) Determine odd or even, where to stop
        if l%2 == 0:
            move = int(l/2)
            move2 = move
        elif l%2 != 0:
            move = int((l+1)/(2))
            move2 = move-1

        # 3) Create Pointer 1, 2. Put them into position
        p1 = head
        p2 = head

        for i in range(move):
            p2 = p2.next


        # 4) Compare the neccessary times
        for j in range(move):
            print("P1: {} P2: {}".format(p1.val, p2.val))
            if p1.val != p2.val:
                return False
            elif p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next


        print(head)
        return True

if __name__ == '__main__':
    # head = ListNode(1)
    # a = ListNode(0)
    # b = ListNode(1)
    #
    # head.next = a
    # a.next = b

    head = ListNode(1)
    a = ListNode(2)
    z = ListNode(3)
    b = ListNode(2)
    c = ListNode(1)

    head.next = a
    a.next = z
    z.next = b
    b.next = c


    ans = Solution()

    r = ans.isPalindrome(head)
    # print(r)
