'''
Given an array of distinct integers arr[int],
and an array of integer arryas


arr: List[int]
pieces: List[List[int]]

So we can pick with element of pieces that we
want to use, however we can't re-order the elements
in pieces.

So loop through the list once, create a hashmap
that contains each element in arr that we are
looking for.

Ok so this problem is actually much easier then I thought
it would be. The number of distinct elements in pieces is
equal to the length of pieces.

arr    = [91,4,64,78]
pieces = [[78],[4,64],[91]]

91 = [2]
4  = [1]
64 = [1]
78 = [0]

So we have this map, we can record what
element in the list that we are at. We can also
record the current element in the map we are at,
we can also store all of the elements that we
have seen previously.

idx = 0
visited_pieces = set()
current_piece = None

# 1) Create Map
Search for arr[idx], if dne or the key is in visited, return False.

# 2)...
Once found element, if the new idx != current idx then add the idx to visited.

If the element that we are looking for is not in the slice, return False

Once found, += 1 to idx, find next element.




'''

class Solution:

    def canFormArrayIII(self, arr, slices):
        map = {}

        # Populate map
        for i in range(len(slices)):
            slice = slices[i]

            for e in slice:
                map[e] = i


        for term in arr:

            if term not in map:
                return False

            slice = slices[map[term]]
            found = False

            for i in range(len(slice)):
                if slice[i] == term:
                    slices[map[term]] = slice[i+1:]
                    found = True
                    break


            if not found:
                return False

        return True

    def canFormArray_II(self, arr, slices):
        map = {e[0]: e for e in slices}

        for term in arr:
            if term not in map:
                return False

            slice = map[term]
            found = False

            for i in range(len(slice)):
                if slice[i] == term:
                    map[term] = slice[i+1:]
                    found = True
                    break

            if not found:
                return False

        return True

        # 50% slower, takes up 100% less memory
    def canFormArrayI(self, arr, pieces):
        map = {}
        idx = 0
        pIdx = 0
        visited_pieces = set()
        current_piece = None
        new_piece = None
        itr = None

        for i in range(len(pieces)):
            piece = pieces[i]

            for e in piece:
                map[e] = i

        while idx < len(arr):
            targ = arr[idx]

            if targ not in map:
                return False

            if current_piece == None:
                current_piece = map[targ]

            elif current_piece != None:

                new_piece = map[targ]

                if new_piece != current_piece and new_piece in visited_pieces:
                    return False

                if new_piece != current_piece:
                    visited_pieces.add(current_piece)
                    current_piece = new_piece
                    pIdx = 0


            itr = pieces[current_piece]

            while pIdx < len(itr):
                if itr[pIdx] == targ:
                    break

                pIdx += 1

            if pIdx >= len(itr):
                return False

            idx += 1

        return True


    def canFormArray(self, arr, slices):
        m = {s[0]:s for s in slices}
        mi = 0
        master = []
        idx = 0
        s = set()

        while idx < len(arr):

            if mi > len(master)-1:
                if arr[idx] not in m:
                    return False

                addition = m[arr[idx]]

                tuple_repr = tuple(addition)

                if tuple_repr in s:
                    return False

                s.add(tuple(addition))
                master += addition

            if master[mi] == arr[idx]:
                idx += 1

            mi += 1

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.canFormArray([85], [[85]]) == True)
    print(s.canFormArray([15, 88], [[88], [15]]) == True)
    print(s.canFormArray([49, 18, 16], [[16,18,49]]) == False)
    print(s.canFormArray([91,4,64,78], [[78],[4,64],[91]]) == True)
    print(s.canFormArray([1, 3, 5, 7], [[2,4,6,8]]) == False)
    print(s.canFormArray([1, 3, 5, 7], [[1, 3, 5, 7]]) == True)

    print(s.canFormArray([1,2,3], [[2],[1,3]]) == False)
