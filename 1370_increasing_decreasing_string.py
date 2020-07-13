'''
Ok so what is the goofy algo that they mentioned?

They talk about picking the smallest character, appending
it to the answer, then picking the next largest number.

Something that we could do is append all of the characters
to a dictionary. Then using the algo on the keys. If we hit
zero, we delete the keys.

So put things in dict.
Sort keys.

Honestly I'm not sure that I got the implementation down.

From lo to high, append elements to ans.
When we get to high, start from high and then go to low.

Start at lo, go lo to hi
start at hi go hi to lo
assuming the number of the character in
the alphabet allows us to order things.

Ok so we go high, then we go lo, then we go hi.

I don't get why this doesn't work.

[a,b,c]

[a,b]

I think I should have two formal forwards/backwards passes
in the for loop.

Sick so I got it right! I forgot what goal I was
going for, all good besides that.

Got it right.

tc: Linear to create the mapping, n log n to sort list.
sp: linear for dict. Linear for merge sort. Linear for ans.


'''

class Solution:
    def sortString(self, s):
        d = {}

        for char in s:
            if char in d:
                d[char] += 1

            elif char not in d:
                d[char] = 1

        keys = list(d.keys())
        keys.sort() # n log n

        ans = ""
        # ans_n = ""
        itr = 1

        i = 0

        # print(d)
        # print(keys)

        while keys:
            # print(keys)
            # print(len(keys))
            if (i > len(keys) - 1) or (i < 0):
                if i < 0:
                    i = 0

                elif i > len(keys) - 1:
                    i = len(keys) - 1

                itr *= -1

            ans += keys[i]
            # ans_n += "({})".format(ord(keys[i]))
            d[keys[i]] -= 1

            if d[keys[i]] == 0:
                # print("Deleting {}".format(keys[i]))
                del keys[i]


                if itr == 1:
                    i -= 1

                # else:
                #     i += 1

                # i += -1*itr

            i += itr

        # print(ans_n)
        return ans

if __name__ == '__main__':
    s = Solution()

    # print(s.sortString("aaaabbbbcccc"))
    print(s.sortString("gtqxozxzrssrzxzoxqtg"))
