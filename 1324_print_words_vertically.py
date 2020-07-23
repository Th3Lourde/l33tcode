
'''

str → list[str]

rows = ["", "", ""]

So what is rows?

rows represents each row in the
verical orientation of our string

if len(e) > len(rows): append "e"
if len(e) == len(rows): rows[i] += e[e]
if len(e) < len(rows): add " " for all missing spaces.

given a string s = "HOW ARE YOU"

s = ["HOW", "ARE", "YOU"]
rows = []

e in ["HOW", "ARE", "YOU"]:

 i = 0

 while i < len(rows) or i < len(e):

     if i > len(rows)-1:
         rows.append(e[i])

     elif i < len(rows) and i < len(e):
         rows[i] = rows[i]+e[i]

     elif i < len(rows) and i >= len(e):
         rows[i] = rows[i]+" "

     i += 1

ret rows

It looks like we made an incorrect assumption.
We should find the word with the greatest length,
create rows, then go from there.

So no appending : )

Got it first time after doing some testing.
Go me. Do more test cases before writing code.

'''


class Solution:
    def printVertically(self, s):
        words = s.split(" ")

        mWidth = 0

        for word in words:
            mWidth = max(mWidth, len(word))

        rows = [""]*mWidth

        for e in words:

            for i in range(len(rows)):

                if i < len(e):
                    rows[i] = rows[i] + e[i]

                elif i >= len(e):
                    rows[i] = rows[i] + " "

        for i in range(len(rows)):
            rows[i] = rows[i].rstrip()

        return rows


if __name__ == '__main__':
    s = Solution()

    print(s.printVertically("HOW ARE YOU"))
    print(s.printVertically("WHO ARE YOU"))

    print(s.printVertically("WHO ARE YU"))

    print(s.printVertically("WHO AE YUE"))

    print(s.printVertically("A XSS AB ACBDA"))

    print(s.printVertically("CONTEST IS COMING"))
