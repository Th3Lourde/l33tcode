'''
So we are given a pattern. What we could do
is count the number of elements that have
a certain frequency.

If we transform it to a frequency map, this gives
us a way to seperate the different strings.

create a function that takes in a string and converts
it to a frequency map. If the two maps are equal
append/return True. If they are not return False.


March through all of the keys and subtract one. If
the sum is zero return True.

"abb" → 1:1, 2:1
sum = 2

"mee" → "m":1, "e":2
Loop through each key:

matches_pattern(s, pattern_dict) (pattern_dict| 1:1, 2:1)

1) Create pattern dict, sum
2) For each words, create dict, update sum, check

pattern_dict = {}
d = "a":1, "b":2

Initial idea was that we break something down, what if we
build something up?

We could create an array instead. Those are easy to tell if
they are equal

index = freq, arr[index] = number of elements at that freq.

This is also incorrect. The frequency and the order of the elements
in the frequency both matter.

----------------------------------------------------------------------------------
7.12.20

How about this:
Two pointers, compare whether or not the current element is
the same as the next element. This will give us the permutation.

We want to track both the number of elements and the order in which
those elements occur.

What we could do is create a mapping from the elements in string one
to the elements in string two.

pattern: "abb"
   werd: "mee"

see two elements, either create mapping or check that the mapping exists.
Then, check the previous elements in order to make sure that they are equal.

"abb" | "mee"
 ^       ^

{}

Have "a" and "m". Check if "a" has a mapping. It does not,
so we add the mapping of "a" → "m"

If "a" does have a mapping, check that the d["a"] == the other
element.

"aba" | "mcd" <-- When we get to the last element, we will see
    that "a" has a mapping and that it doesn't equal "d". Thus
    we return False.


1) Check or add mapping.
2) Check that the previous element matches?
    Do we even need to do this?

{}
"abb" | "mee"
 ^       ^
{"a":"m"}

{"a":"m"}
"abb" | "mee"
  ^       ^
{"a":"m", "b":"e"}

"abb" | "mee"
   ^       ^
{"a":"m", "b":"e"}
Return true.

Let's do another example just to make sure

"abb" | "ccc"
 ^       ^
{"a":"c"}

{"a":"c"}
"abb" | "ccc"
  ^       ^
{"a":"c"} <-- we would put "c" in used, thus when creating
            the mapping for "b" we would realize that we
            couldn't do so.


So also have a dict of terms that we have used?

mapping = {}
used = {}


"abb" | "abc"
 ^       ^

mapping = {}
used = {}
"abb" | "abc"
 ^       ^

mapping = {"a":"a"}
used = {"a"}
"abb" | "abc"
  ^       ^

mapping = {"a":"a", "b":"b"}
used = {"a":True, "b":True}
"abb" | "abc"
   ^       ^

mapping = {"a":"a", "b":"b"} <-- Check used when we are creating a new key value pair for mapping.
used = {"a":True, "b":True}
"abb" | "abc"
   ^       ^
We have a mapping for "b", however the p2-value doesn't equal that value. So we return False.

Check length, if not same length, return False.

create empty mapping {}, empty used {}.
pointer one first element of s1, s2.

while iterating through both strings:
    if p1 is in mapping, check that the mapping is equal to p2. If yes, continue. If not, return False
    if p2 is not in mapping, check that p2 is available to use. If yes, create new mapping. If not, return False

After we have seen all elements, return True.

def iso_exists(word, pattern):
    if len(word) != len(pattern): return False

    mapping = {}
    used = {}

    for i in range(len(word)):
        if pattern[i] in mapping:
            if mapping[pattern[i]] != word[i]:
                return False

        elif pattern[i] not in mapping:
            if word[i] in used:
                return False

            mapping[pattern[i]] = word[i]
            used[word[i]] = True

    return True

Ok test case time.
Any word of a different length gets
thrown out.

Same frequency but different perm gets thrown out.

We can vary the number of unique elements
We can vary the frequency of said unique
elements.
We can vay the position of said unique elements

I am convinced that my code takes all three of these into
consideration/solves the problem for all three of these
cases.

Let's do some more testing in the LC client, then submit.

Ok I got it right. What is the time complexity/space complexity?

tc: 0(n*(length of each element))
sp: 0(space of pattern + 2*space of word)



'''

class Solution:
    def findAndReplacePattern(self, words, pattern):
        def iso_exists(word, pattern):
            if len(word) != len(pattern): return False

            mapping = {}
            used = {}

            for i in range(len(word)):
                if pattern[i] in mapping:
                    if mapping[pattern[i]] != word[i]:
                        return False

                elif pattern[i] not in mapping:
                    if word[i] in used:
                        return False

                    mapping[pattern[i]] = word[i]
                    used[word[i]] = True

            return True


        ans = []

        for word in words:
            if iso_exists(word, pattern):
                ans.append(word)

        return ans

    def findAndReplacePattern_1(self, words, pattern):
        d = {}
        pattern_dict = {}
        empty = {}
        ans = []

        for e in pattern:
            if e in d:
                d[e] += 1

            else:
                d[e] = 1

        # print(d)
        summ = 0
        maxKey = 0

        for key in d:
            if d[key] in pattern_dict:
                pattern_dict[d[key]] += 1
                maxKey = max(maxKey, d[key])

            else:
                pattern_dict[d[key]] = 1
                maxKey = max(maxKey, d[key])


        # print(pattern_dict)
        # print(maxKey)
        cmpr = [0]*(maxKey+1)
        # print(summ)
        # print(empty)

        for i in range(1, maxKey+1):
            if i in pattern_dict:
                cmpr[i] = pattern_dict[i]

        # print(cmpr)


        def helper(s, arr):
            # print(s)
            pattern_dict = {}
            tmp = {}

            for e in s:
                if e in tmp:
                    tmp[e] += 1
                else:
                    tmp[e] = 1

            maxKey = 0

            for key in tmp:
                if tmp[key] in pattern_dict:
                    pattern_dict[tmp[key]] += 1
                    maxKey = max(maxKey, tmp[key])

                else:
                    pattern_dict[tmp[key]] = 1
                    maxKey = max(maxKey, tmp[key])

            cmpr = [0]*(maxKey+1)

            # print(maxKey)
            # print(pattern_dict)

            for i in range(1, maxKey+1):
                if i in pattern_dict:
                    cmpr[i] = pattern_dict[i]

            # print(cmpr)
            return cmpr == arr




        ans = []

        for word in words:
            if helper(word, cmpr):
                ans.append(word)

        return ans


# def iso_exists(word, pattern):
#     if len(word) != len(pattern): return False
#
#     mapping = {}
#     used = {}
#
#     for i in range(len(word)):
#         if pattern[i] in mapping:
#             if mapping[pattern[i]] != word[i]:
#                 return False
#
#         elif pattern[i] not in mapping:
#             if word[i] in used:
#                 return False
#
#             mapping[pattern[i]] = word[i]
#             used[word[i]] = True
#
#     return True

# iso_exists("","abb")
# iso_exists("cdd","abb")
# iso_exists("mee","abb")
# iso_exists("aqq","abb")
# iso_exists("ccc","abb")
# iso_exists("ccd","abb")
# iso_exists("cdd","abb")
# iso_exists("dcd","abb")


if __name__ == '__main__':
    s = Solution()
    # print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
    print(s.findAndReplacePattern([], "abb"))
    # print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "xcccabbzzz"))
