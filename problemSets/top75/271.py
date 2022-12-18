'''
Design an algorithm to encode a list of strings to a string
the dencoded string is then sent over the network and decoded
back to the original list of strings.

So we want a string that we can used as our sep that won't
be present in the strs that we are given.

That prob would pass this funciton, however we are still guessing.

We could come up with a sep until the sep isn't in the given strs.
That would work

then append the sep to the end of the str (|sep)
'''

import random

class Codec:
    def encode(self, strs):
        # s = set()
        #
        # for word in strs:
        #     for idx in range(1, len(word)+1):
        #         s.add(word[0:idx])
        #
        # sep = str(len(strs))
        #
        # while sep in s:
        #     randInt = random.randint(97, 122)
        #     sep += chr(randInt)
        #
        # resp = sep.join(strs)
        # return resp + "|{}".format(sep)

        resp = []

        for word in strs:
            for chr in word:
                resp.append(str(ord(chr)))
            resp.append("|")

        return ",".join(resp)


    def decode(self, s):
        # lastIdx = len(s)-1
        #
        # while s[lastIdx] != '|':
        #     lastIdx -= 1
        #
        # s, sep = s[0:lastIdx], s[lastIdx+1:]
        #
        # return s.split(sep)
        resp = []
        word = []
        splitS = s.split(",")

        for ascii in splitS:
            if ascii == "|":
                resp.append("".join(word))
                word = []
            else:
                word.append(chr(int(ascii)))

            # resp.append(chr(int(ascii)))

        return resp

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        for s in strs:
            answer += str(len(s)) + ":" + s

        return answer


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i+1:]
            strs.append(s[:length])
            s = s[length:]
        return strs


cd = Codec()

# en = cd.encode(["123"])
en = cd.encode(["123:321:Hello", "World"])
# en = cd.encode(["6*2", "6*3"])

en

cd.decode(en)


a = ["a", "b", "c"]
",".join(a)
