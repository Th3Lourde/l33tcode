
'''
Given an integer, n, add a dot → as the
thousands separator.

So start from rhs of the string, every three times,
insert a "." (iff there is an element on the rhs)
and then continue

For loop, rhs.

Mod is prob more trouble than it's worth.

Have some kind of local cntr instead.

Split into a list? We can't just insert.






'''

class Solution:
    def thousandSeparator(self, n):
        n = str(n)
        nList = list(n)
        cntr = 1

        i = len(nList)-1

        while i > 0:
            if cntr == 3 and i != 0:
                nList.insert(i, ".")
                cntr = 1
                i -= 1

            cntr += 1

            i -= 1

        return "".join(nList)


if __name__ == '__main__':
    s = Solution()

    print(s.thousandSeparator("987"))

    print(s.thousandSeparator("1234"))

    print(s.thousandSeparator("123456789"))

    print(s.thousandSeparator("123456789123456789123456789"))

    print(s.thousandSeparator("0"))
