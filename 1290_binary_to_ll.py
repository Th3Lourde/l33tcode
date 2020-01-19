

class Solution:
    def getDecimalValue(self, head):
        if head == None:
            return None

        bins = []

        while True:

            if head == None:
                break

            elif head != None:
                bins.append(str(head.val))
                head = head.next


        bin_str = "".join(bins)

        return int(bin_str, 2)













if __name__ == '__main__':
    s = Solution()

    print(s.getDecimalValue([1,0,1]))
