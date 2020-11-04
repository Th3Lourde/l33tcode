'''
So all we really care about is
creating a UUID that is at the
end of the URI.

Let's just generate a random string of length l,
check if we have already used the string that we
created. If we have, create another one.

0 → 9 | 49-57
a → z | 97-122

Let's do length 6, 2 ints, 4 chars

For ints, just pick a number between [0,9]

For chars, pick a number ∈ [97, 122]

Should we remember what URLs we have already
stored? Sounds like no.

So every time we are given a url, return the
new link.

When given the new link, return the url.

If we are given the same url more than once,
we output two new links.

'''
import random as r

class Codec:

    def __init__(self):
        self.idToLink = {}

    def create_code(self):
        id = ["" for i in range(6)]

        for i in range(2):
            num = r.randint(0,9)
            idx = r.randint(0,5)

            while id[idx] != "":
                idx = r.randint(0,5)

            id[idx] = str(num)

        for i in range(len(id)):
            if id[i] == "":
                char = r.randint(97,122)
                id[i] = chr(char)

        url = "".join(id)

        return url

    def encode(self, longUrl):
        url = self.create_code()

        while url in self.idToLink:
            url = self.create_code()

        self.idToLink[url] = longUrl

        return "http://tinyurl.com/" + url


    def decode(self, shortUrl):

        return self.idToLink[shortUrl[-6:]]

if __name__ == '__main__':
    c = Codec()

    url = c.encode("asdfa")

    c.decode(url)
