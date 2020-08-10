# Ok I totally killed this. Go me.
# I'm finally getting a bit better at these.
# Let's do another couple weeks, let's get
# reallll good : )
class CombinationIterator:
    def __init__(self, chars, n):
        chars = list(chars)
        # chars.sort()

        self.perms = []

        def itr(p, opt):
            if len(p) == n:
                self.perms.append(p)
                return

            elif len(p) != n:
                for i in range(len(opt)):
                    tmp = str(p)+opt[i]
                    # itr(tmp, opt[:i]+opt[i+1:])
                    itr(tmp, opt[i+1:])

        itr("", chars)

        self.idx = 0

    def next(self):
        resp = self.perms[self.idx]
        self.idx += 1

        return resp

    def hasNext(self):
        return self.idx < len(self.perms)


if __name__ == '__main__':
    s = CombinationIterator("abc", 2)

    s.next()
    s.hasNext()

    s.next()
    s.hasNext()

    s.next()
    s.hasNext()
