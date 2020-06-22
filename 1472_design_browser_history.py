'''
Ok so we are designing/implementing a browser history
class.

Initialized with the current page that we are on.

visit (go to url; clear all forward history)

back (k), go back k steps. If the number of backs < k
return the last back.

forward (k), same as back, only for forwards

thoughts:
have .current = str , .back = [], .forward = []

init (leetcode.com)

self.current = leetcode.com

algo for back:

while-loop, while back != [] and we have not done k-times:
    push current to forward
    current = back.pop()
    itr += 1

return current

k = 4

[] a [b,c,d,e,f,g]

i = 2

------------------------------
k = 4


[a,b,c] d [g,f,e]

a    d    e
b         f
c         g

d    e    f
a         g
b
c

So what test cases can we run?
- init, make sure things are initialized correctly
|--> Done

- visit
|--> add current to rhs of back, update new link, delete forwardS
|--> Done

- back (1)
- if back != [], send current to lhs of forwards, current = rhs of back, pop from back
|--> Done

I also checked back and forward. Current is updated as should be. No terms are lost.

'''

class BrowserHistory: # Passes

    def __init__(self, homepage):
        self.backS = []
        self.forwardS = []
        self.current = homepage

    def __repr__(self):
        return "{} {} {}".format(self.backS, self.current, self.forwardS)

    def visit(self, url):
        self.backS.append(self.current)
        self.current = url
        self.forwardS = []


    def back(self, steps):
        i = 0

        while self.backS != [] and i < steps:
            self.forwardS.append(self.current)
            self.current = self.backS.pop()
            i += 1

        return self.current


    def forward(self, steps):
        i = 0

        while self.forwardS != [] and i < steps:
            self.backS.append(self.current)
            self.current = self.forwardS.pop()
            i += 1

        return self.current

if __name__ == '__main__':
    bh = BrowserHistory('leetcode.com')

    bh.visit('google.com')
    bh.visit('facebook.com')
    bh.visit('youtube.com')

    bh

    bh.forward(3)
    bh.back(3)
