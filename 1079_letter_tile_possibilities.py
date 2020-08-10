
class Solution:
    def numTilePossibilities(self, tiles):

        def itr(s, opt):
            for i in range(len(opt)):
                s2 = s+opt[i]
                unq.add(s2)
                itr(s2, opt[0:i]+opt[i+1:])

        unq = set()

        itr("", tiles)

        return len(unq)


if __name__ == '__main__':
    s = Solution()

    # print(s.numTilePossibilities("AAB"))

    print(s.numTilePossibilities("AAABBC"))
