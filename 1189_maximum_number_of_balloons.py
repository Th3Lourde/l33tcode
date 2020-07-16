'''
Given a string, return how many times
we can create the word "balloon".

Ok so what we could do is create too dicts.

One dict for char --> freq
one dict for freq --> num of chars
  two dicts for this, the number of chars
  required is different

We need one of {b,a,n}
We need two of {l,o}

e.g.

"nlaebolko"
 ^

b: 0, a: 0, l: 0, o: 0, n: 0
ones = {}
twos = {}

"nlaebolko"
  ^

b: 0, a: 0, l: 1, o: 0, n: 0
ones = {1: 1} <-- care about the min?

"nlaebolko"
   ^

b: 0, a: 1, l: 1, o: 0, n: 0

Can just keep dict, we know what we are
trying to spell.

min of {b,a,n}
min of {l,o}/2 <--math.floor

"nlaebolko" --> {b:1, a:1, l:2, o:2, n:1}

Initialize dict to be zero initially

m1 = d['b']

for e in ["a","n"]:
    m1 = min(m1, d[e])

m2 = min(math.floor(d["l"]/2), math.floor(d["o"]/2) )

return min(m1, m2)




'''
import math

class Solution:
    def maxNumberOfBalloons(self, text):
        d = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for e in text:
            if e in d:
                d[e] += 1

        m1 = d["b"]

        for e in ["a","n"]:
            m1 = min(m1, d[e])

        return min(m1, math.floor(min(d["l"], d["o"])/2) )


if __name__ == '__main__':
    s = Solution()

    print(s.maxNumberOfBalloons("nlaebolko"))
    print(s.maxNumberOfBalloons("loonbalxballpoon"))
    print(s.maxNumberOfBalloons("leetcode"))

    print(s.maxNumberOfBalloons(""))

    print(s.maxNumberOfBalloons("anollbbaloonlo"))
