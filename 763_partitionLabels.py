'''
Given a string of lowerCase English letters.

Partition the string ∋ the intersection of each
partition is the empty set.

One loop, to create a dict d[chr] = frequency

For every partition, create another dict that keeps
track of the elements in the current parition.

Whenever the keys of the partition have the same values
as the keys in the initial dict, drop a partiton.

An easy way to verify that we have enough elements
would be to perform a comparison instead of iter.

Every time we see a new element, add initial[element] = frequency
to another dict.

e.g. :

d ← dict from first loop

part ← dict representing partition
done ← dict representing what part looks like when ready to split

done[a] = d[a]

part == done ⟹ make a partition.





'''

class Solution:
    def partitionLabels(self, s):
        d = {}

        for chr in s:
            if chr not in d:
                d[chr] = 1
            else:
                d[chr] += 1

        ans = []

        p = {}
        done = {}
        part = -1

        for i in range(len(s)):
            e = s[i]

            if e in p:
                p[e] += 1

            else:
                p[e] = 1
                done[e] = d[e]

            if p == done:
                ans.append(i-part)
                part = i
                p = {}
                done = {}

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
