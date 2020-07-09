'''
Given a list of words, return the k most frequently
occurring words

If the words have the same frequency, sort by
alphabetical order.

throw all elements into a dict.

Go through all of the keys in the dict and sort the
values in alphabetical order.

Then sort the keys.

Then pop from the different keys

w : 4
d : 4

f : 3
g : 3

a : 2
b : 2
z : 2
e : 2

"w","w","w","w",
"d","d","d","d",

"f","f","f",
"g","g","g",

"a","a",
"b","b",
"z","z",
"e","e",


["w","w","w","w", "d","d","d","d", "f","f","f", "g","g","g", "a","a", "b","b", "z","z", "e","e"]
'''
class Solution:
    def topKFrequent(self, words, k):
        d = {}

        for word in words:
            try:
                d[word] += 1

            except:
                d[word] = 1

        # print(d)

        f = {}

        for key in d:
            try:
                f[d[key]].append(key)

            except:
                f[d[key]] = [key]

        keys = list(f.keys())
        keys.sort(reverse=True)

        # print(f)

        ans = []
        z = 0

        for key in keys:
            if len(f[key]) > 1:
                f[key].sort()

            # print(f[key])

            for e in f[key]:

                if z == k: return ans

                ans.append(e)

                z += 1

        print(ans)


if __name__ == '__main__':
    s = Solution()
    s.topKFrequent(["a","b","a","b","c","d"], 5)
