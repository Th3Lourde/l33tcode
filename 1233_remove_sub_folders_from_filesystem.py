'''
Given a list of folders, remove all
sub-folders in those folders and return in any
order the folders after removing.

In: /a, /a/b, /c/d, /c/d/e, /c/f

/a/b    is in /a
/c/d/e  is in /c/d

we seperate folders by '/'
What we might want to do is to

sort the list by folders with the
shortest paths

/c/d and /c/f are included because
they are distinct folders. If we had
/c, we would not include them.

One pass to put the folders in a dict {}
key: len of path, val, [paths]

Then loop through the different paths, using
the dictionary to determine which folders we
include and which folders we do not include.

Given /a, /a/b, how do we know that we do not
include /a/b?

We can check each element of the path against
the dict to see if we have the folder already.

1) Put everything into a dict, by len of path
2) Loop through the different lengths of paths
   create another dict, store the path as key,
   True as val.

2itr) For every path, query each folder combo
in the path to see if we have encountered it
already.

then return the keys of the second dict as our
answer. Runtime: 0(n*(number of elements per term)) + 0(n * (number of levels per term < n))

Ex:
["/a","/a/b","/c/d","/c/d/e","/c/f"]

pass 1: dict

{ 1 : ["/a"], 2 : ["/a/b", "/c/d", "c/f"], 3: ["/c/d/e"] }

pass 2: create answer

{}

1: ["/a"]
"/a" not in dict, add it

{"/a"}

2: ["/a/b", "/c/d", "c/f"]
"/a/b", /a in dict, next
"/c/d" not in dict, add it
"/c/f" not in dict, add it

{"/a":True, "/c/d":True, "/c/f":True}

3: ["/c/d/e"]
"/c/d/e", "/c" not in dict, "/c/d" in dict
next

return keys of dict: ["/a", "/c/d", "/c/f"]

The assumption that I made that was incorrect
was that the size of the paths would start at
one. This isn't the case.

We could probably use an indexed heap in order
to solve this. When we encounter a new 'lenth',
we throw it into our min heap. Use dict to keep
track of sizes that we have alread seen?

If we have already seen it, append it to
the heap element.

Eliminates the need for us to sort the keys
of the dictionary.

'''




class Solution:
    def removeSubfolders(self, folder): # Works, is very slow, but works. Made a few mistakes.
                                        # So this is a trie problem. Lol.

        d = {}

        for path in folder:
            # Get 'level'
            level = 1

            i = 1
            while i < len(path):
                if path[i] == "/":
                    level += 1
                i += 1

            try:
                d[level].append(path)

            except:
                d[level] = [path]

        d2 = {}

        keys = list(d.keys())
        keys.sort()

        for i in keys:

            terms = d[i]

            for term in terms:
                z = 1
                hit = False

                path = "/"

                while z < len(term):
                    if term[z] == "/":
                        try:
                            if d2[path]:
                                hit = True
                                break

                        except:
                            ...

                    path = path + term[z]
                    z += 1

                if hit == False:
                    d2[term] = True


        return list(d2.keys())


if __name__ == '__main__':
    s = Solution()
    s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])
    s.removeSubfolders(["/a/b/cd", "/a/b/c", "/a/b", "/a"])

    '''
    So I think I got it. Let's come up with some testcases
    and make sure we didn't miss anything. So I caught a
    bug. Good. Write more test cases.

    ["/a","/a/b","/c/d","/c/d/e","/c/f"]  | ["/a","/c/d","/c/f"]
    ["/a","/a/b/c","/a/b/d"] | ["/a"]
    ["/a/b/c","/a/b/ca","/a/b/d"] | ["/a/b/c","/a/b/ca","/a/b/d"]
    ["/a/b/cd", "/a/b/c", "/a/b", "/a"]

    '''
